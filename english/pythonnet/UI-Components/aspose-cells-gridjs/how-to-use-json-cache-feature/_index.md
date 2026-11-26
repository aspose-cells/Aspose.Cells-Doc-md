---
title: How to Use JSON Cache Feature in GridJs  
type: docs
weight: 250
url: /python-net/aspose-cells-gridjs/how-to-use-json-cache
description: This article describes how to enable and configure the JSON cache feature in GridJs to speed up repeated data requests.
keywords: GridJs, json cache, cache, performance, optimize loading
aliases:
  - /python-net/aspose-cells-gridjs/jsoncache/
  - /python-net/aspose-cells-gridjs/json-cache/
  - /python-net/aspose-cells-gridjs/use-cache/

ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## About JSON Cache

Every time a spreadsheet is displayed or refreshed, GridJs converts the workbook into a JSON string. For large files this conversion can be expensive. The **JSON Cache** feature stores the generated JSON so that subsequent requests for the same data are served directly from the cache, without re-parsing the workbook. This can make repeated requests several times faster.

The cache is a two-level (L1 + L2) design:

| Level | Storage | Eviction |
|-------|---------|----------|
| L1 | In-memory (LRU dictionary, shared by all `GridJsWorkbook` instances) | TTL (`MemoryTtl`, default 1 hour) and size limit (`MaxMemoryEntries`, default 1000) |
| L2 | Disk files (optionally Gzip compressed) | TTL (`DiskTtl`, default 24 hours) and total size limit (`MaxDiskSizeMB`, default 500 MB, oldest files removed first) |

When a cache read misses L1 but hits L2, the JSON is loaded from disk and promoted back into memory. Writes to disk happen asynchronously in the background, so they never block the response.

Each disk entry consists of a data file plus a small sidecar metadata file that records the original cache key. Both are created and removed automatically by the cache, and both are what makes invalidation and cleanup work without any in-memory state — see [Invalidate the Cache](#step-3-invalidate-the-cache-when-data-changes) and [Proactive Cleanup](#step-4-proactively-clean-up-expired-cache-files).

The cache is automatically used by the data-loading APIs, for example:

- `detail_stream_json_with_uid` / `detail_file_json_with_uid` — caches the whole workbook JSON (cache key `gridjs_json_{uid}_{fileName}`).
- `lazy_loading_stream_json` / `lazy_loading_json` — caches JSON per sheet (cache key `gridjs_json_{uid}_{fileName}_{sheetName}`).
- `json_to_stream` — workbook JSON generated in stream mode is also cached and reused.

Workbook-level and sheet-level entries use different keys, so mixing detail loading and lazy loading for the same file never returns the wrong JSON.

> **Note:** Caching only takes effect when both a `uid` and a file name are available for the request. When `enable = False` (the default), nothing is cached and behavior is unchanged.

## Configuration Options

All options are provided by the `JsonCacheOptions` class, reachable through the static `Config.json_cache` or the per-instance `GridJsOptions.json_cache` — both have the same effect.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `enable` | bool | `False` | Master switch. Must be `True` for any caching to happen. |
| `implementation` | IGridJsJsonCache | `None` | Custom cache storage. If not set, the built-in `DefaultGridJsJsonCache` (memory + disk) is used. |
| `max_memory_entries` | int | 1000 | Maximum number of entries kept in memory (L1). |
| `memory_ttl` | long | 1 hour | Lifetime of an in-memory entry, in minutes (default: 60) |
| `enable_disk` | bool | `True` | Whether the disk cache (L2) is used. |
| `disk_path` | string | `[file_cache_directory]/json_cache` | Directory that stores disk cache files. |
| `max_disk_size_mb` | long | 500 | Maximum total size of the disk cache; oldest files are deleted beyond this limit. |
| `disk_ttl` | long | 24 hours | Lifetime of a disk cache file, in minutes (default: 24*60) |
| `compress_disk` | bool | `True` | Whether disk cache files are Gzip compressed. |

## Implementation Steps

### Step 1: Enable JSON Cache in Flask App Setup

**Example using Config:**

```python
from aspose.cells.gridjs import Config

Config.json_cache.enable = True
```

**Example using GridJsOptions (Flask DI via app context):**

```python
from flask import Flask
from aspose.cells.gridjs import GridJsOptions, Config
import os

def create_app():
    app = Flask(__name__)
    app.config['JSON_CACHE_ENABLE'] = True
    app.config['JSON_CACHE_ENABLE_DISK'] = True
    app.config['JSON_CACHE_DISK_PATH'] = os.path.join(os.getcwd(), 'gridjs_json_cache')  # optional, defaults to [file_cache_directory]/json_cache
    app.config['JSON_CACHE_MAX_MEMORY_ENTRIES'] = 1000
    app.config['JSON_CACHE_MEMORY_TTL'] = 3600  # 1 hour in seconds
    app.config['JSON_CACHE_MAX_DISK_SIZE_MB'] = 500
    app.config['JSON_CACHE_DISK_TTL'] = 86400  # 24 hours in seconds
    app.config['JSON_CACHE_COMPRESS_DISK'] = True

    # Configure GridJsOptions via app context
    @app.before_first_request
    def initialize_gridjs_options():
        options = GridJsOptions()
        options.json_cache.enable = app.config['JSON_CACHE_ENABLE']
        options.json_cache.enable_disk = app.config['JSON_CACHE_ENABLE_DISK']
        options.json_cache.disk_path = app.config['JSON_CACHE_DISK_PATH']
        options.json_cache.max_memory_entries = app.config['JSON_CACHE_MAX_MEMORY_ENTRIES']
        options.json_cache.memory_ttl = app.config['JSON_CACHE_MEMORY_TTL']
        options.json_cache.max_disk_size_mb = app.config['JSON_CACHE_MAX_DISK_SIZE_MB']
        options.json_cache.disk_ttl = app.config['JSON_CACHE_DISK_TTL']
        options.json_cache.compress_disk = app.config['JSON_CACHE_COMPRESS_DISK']
        Config.json_cache = options.json_cache  # Assign to static Config for global access

    return app
```

### Step 2: Use the Normal Loading APIs

No client-side change is required. Once the cache is enabled, the `GridJsService` loading APIs check the cache before generating JSON and store the result afterwards:

```python
from flask import Flask, request, Response
from aspose.cells.gridjs import IGridJsService, GridJsService
import os

app = Flask(__name__)
gridjs_service = GridJsService()

@app.route('/detail-stream-json-with-uid', methods=['POST'])
def detail_stream_json_with_uid():
    filename = request.form.get('filename')
    uid = request.form.get('uid')
    if not filename or not uid:
        return "filename and uid are required", 400

    file_path = os.path.join("C:\\Files", filename)

    # First call: cache miss -> JSON is generated and cached
    # Second and later calls with the same uid/file: served directly from cache
    response = Response()
    with response.stream as gzip_stream:
        gridjs_service.detail_stream_json_with_uid(gzip_stream, file_path, uid)
    return response
```

### Step 3: Invalidate the Cache When Data Changes

GridJs automatically clears the cached JSON whenever the data is modified through the built-in editing operations of `GridJsService` (`update_cell`, image operations, etc.), so stale JSON is never returned to the client.

If you modify the workbook out of band (for example, the file on disk was replaced by your own code), clear the cache explicitly:

```python
# Clear all cached entries belonging to one loaded file
gridjs_service.clear_json_cache_for_uid(uid)

# Clear every cached entry (memory + disk)
gridjs_service.clear_all_json_cache()
```

`clear_json_cache_for_uid` is disk-aware: it also removes the cached files of a workbook that is **not currently open in memory** — for example after a server restart, when the source file was deleted and never reopened. It matches every cache key belonging to the `uid`, so both workbook-level and sheet-level entries are removed and no sheet names are needed.

### Step 4: Proactively Clean Up Expired Cache Files

Disk entries expire after `disk_ttl`, but the check is lazy: an expired file is deleted when it is read again. Files of workbooks that are never reopened would otherwise stay on disk until the `max_disk_size_mb` limit evicts the oldest ones. To reclaim that space on your own schedule, call:

```python
# Deletes expired data files and their metadata, orphaned metadata, and stale temp files
removed = gridjs_service.purge_expired_json_cache()
```

The method returns the number of deleted files. It skips entries written within the last 10 minutes so it never races with a background write, which makes it safe to call at any time. GridJs deliberately does not start a background thread of its own — scheduling is left to the host application, typically at startup and/or from a scheduler:

```python
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
scheduler.add_job(lambda: gridjs_service.purge_expired_json_cache(), 'interval', hours=1)
scheduler.start()
```

## Using a Custom Cache Implementation (Redis, etc.)

If you want to store the JSON in your own infrastructure — for example a distributed Redis cache — implement the `IGridJsJsonCache` interface and assign it to `implementation`:

```python
from aspose.cells.gridjs import IGridJsJsonCache

class RedisJsonCache(IGridJsJsonCache):
    def __init__(self):
        # Initialize Redis client or other storage
        pass

    def get_cache_key(self, uid: str, file_name: str) -> str:
        # Decide the key strategy:
        # - file_name only -> the same file can share cache across different uids
        # - uid + file_name -> strict isolation per loaded instance
        return f"gridjs_json_{uid}_{file_name}" if file_name else f"gridjs_json_{uid}"

    def try_get_json(self, cache_key: str) -> str:
        # Return cached JSON or None if not found
        return None  # Implement actual Redis or storage logic

    def set_json(self, cache_key: str, json: str):
        # Store JSON
        pass  # Implement actual Redis or storage logic

    def invalidate(self, cache_key: str):
        # Remove one entry
        pass  # Implement actual Redis or storage logic

    def invalidate_all_for_uid(self, uid: str):
        # Remove all entries whose key contains uid
        pass  # Implement actual Redis or storage logic

    def clear_all(self):
        # Remove everything
        pass  # Implement actual Redis or storage logic
```

```python
from aspose.cells.gridjs import Config

Config.json_cache.enable = True
Config.json_cache.implementation = RedisJsonCache()
```

> **Note:** When the `GridJsService` is created from a `GridJsOptions` instance, that instance is copied onto the static `Config.json_cache` field by field, so register the implementation on the options object the service is built with rather than on `Config` alone.

When `implementation` is set, GridJs uses it exclusively and the built-in memory/disk options (`max_memory_entries`, `disk_path`, and so on) are ignored. Expiration and cleanup are then your responsibility as well: `purge_expired_json_cache` is implemented by the built-in cache only and returns 0 for a custom implementation.

## Performance Results

Measured on the product's own regression tests (a small workbook, repeated `detail_stream_json_with_uid` calls with the same uid):

- First call (cache miss): full parse + JSON generation time.
- Second call (cache hit): typically **more than 2x faster**, and the benefit grows with workbook size since the JSON is returned without touching the workbook model at all.

## Demo and Examples

For comprehensive implementation examples and detailed usage scenarios, refer to the official demo repository:

https://github.com/aspose-cells/Aspose.Cells.Grid-for-Python-via-.NET/tree/main/Examples.GridJs

## Additional Resources

- [GridJs Server API Documentation](https://reference.aspose.com/cells/python-net/aspose.cellsgridjs)
- [How to Implement Lazy Loading in GridJs](https://docs.aspose.com/cells/python-net/aspose-cells-gridjs/how-to-do-lazy-loading/)
- [GridJs Client API Documentation](https://docs.aspose.com/cells/python-net/aspose-cells-gridjs/how-to-use-gridjs-client-api)