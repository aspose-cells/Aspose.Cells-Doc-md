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

The cache is automatically used by the data-loading APIs, for example:

- `DetailStreamJsonWithUid` / `DetailFileJsonWithUid` — caches the whole workbook JSON (cache key `gridjs_json_{uid}_{fileName}`).
- `LazyLoadingStreamJson` / `LazyLoadingJson` — caches JSON per sheet (cache key `gridjs_json_{uid}_{fileName}_{sheetName}`).
- `JsonToStream` — workbook JSON generated in stream mode is also cached and reused.

Workbook-level and sheet-level entries use different keys, so mixing detail loading and lazy loading for the same file never returns the wrong JSON.

> **Note:** Caching only takes effect when both a `uid` and a file name are available for the request. When `Enable = false` (the default), nothing is cached and behavior is unchanged.

## Configuration Options

All options are provided by the `JsonCacheOptions` class, reachable through the static `Config.JsonCache` or the per-instance `GridJsOptions.JsonCache` — both have the same effect.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `Enable` | bool | `false` | Master switch. Must be `true` for any caching to happen. |
| `Implementation` | IGridJsJsonCache | `null` | Custom cache storage. If not set, the built-in `DefaultGridJsJsonCache` (memory + disk) is used. |
| `MaxMemoryEntries` | int | 1000 | Maximum number of entries kept in memory (L1). |
| `MemoryTtl` | long | 1 hour | Lifetime of an in-memory entry,, in minutes (default: 60) |
| `EnableDisk` | bool | `true` | Whether the disk cache (L2) is used. |
| `DiskPath` | string | `[FileCacheDirectory]/json_cache` | Directory that stores disk cache files. |
| `MaxDiskSizeMB` | long | 500 | Maximum total size of the disk cache; oldest files are deleted beyond this limit. |
| `DiskTtl` | long | 24 hours | Lifetime of a disk cache file, in minutes (default: 24*60) |
| `CompressDisk` | bool | `true` | Whether disk cache files are Gzip compressed. |

## Implementation Steps

### Step 1: Enable JSON Cache in Flask App Setup

**Example using Config:**

```python
from aspose.cells.gridjs import Config

Config.JsonCache.Enable = True
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
    app.config['JSON_CACHE_DISK_PATH'] = os.path.join(os.getcwd(), 'gridjs_json_cache')  # optional, defaults to [FileCacheDirectory]/json_cache
    app.config['JSON_CACHE_MAX_MEMORY_ENTRIES'] = 1000
    app.config['JSON_CACHE_MEMORY_TTL'] = 3600  # 1 hour in seconds
    app.config['JSON_CACHE_MAX_DISK_SIZE_MB'] = 500
    app.config['JSON_CACHE_DISK_TTL'] = 86400  # 24 hours in seconds
    app.config['JSON_CACHE_COMPRESS_DISK'] = True

    # Configure GridJsOptions via app context
    @app.before_first_request
    def initialize_gridjs_options():
        options = GridJsOptions()
        options.JsonCache.Enable = app.config['JSON_CACHE_ENABLE']
        options.JsonCache.EnableDisk = app.config['JSON_CACHE_ENABLE_DISK']
        options.JsonCache.DiskPath = app.config['JSON_CACHE_DISK_PATH']
        options.JsonCache.MaxMemoryEntries = app.config['JSON_CACHE_MAX_MEMORY_ENTRIES']
        options.JsonCache.MemoryTtl = app.config['JSON_CACHE_MEMORY_TTL']
        options.JsonCache.MaxDiskSizeMB = app.config['JSON_CACHE_MAX_DISK_SIZE_MB']
        options.JsonCache.DiskTtl = app.config['JSON_CACHE_DISK_TTL']
        options.JsonCache.CompressDisk = app.config['JSON_CACHE_COMPRESS_DISK']
        Config.JsonCache = options.JsonCache  # Assign to static Config for global access

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
        gridjs_service.DetailStreamJsonWithUid(gzip_stream, file_path, uid)
    return response
```

### Step 3: Invalidate the Cache When Data Changes

GridJs automatically clears the cached JSON whenever the data is modified through the built-in editing operations of `GridJsService` (`UpdateCell`, image operations, etc.), so stale JSON is never returned to the client.

If you modify the workbook out of band (for example, the file on disk was replaced by your own code), clear the cache explicitly:

```python
# Clear all cached entries belonging to one loaded file
gridjs_service.ClearJsonCacheForUid(uid)

# Clear every cached entry (memory + disk)
gridjs_service.ClearAllJsonCache()
```

## Using a Custom Cache Implementation (Redis, etc.)

If you want to store the JSON in your own infrastructure — for example a distributed Redis cache — implement the `IGridJsJsonCache` interface and assign it to `Implementation`:

```python
from aspose.cells.gridjs import IGridJsJsonCache

class RedisJsonCache(IGridJsJsonCache):
    def __init__(self):
        # Initialize Redis client or other storage
        pass

    def GetCacheKey(self, uid: str, fileName: str) -> str:
        # Decide the key strategy:
        # - fileName only -> the same file can share cache across different uids
        # - uid + fileName -> strict isolation per loaded instance
        return f"gridjs_json_{uid}_{fileName}" if fileName else f"gridjs_json_{uid}"

    def TryGetJson(self, cacheKey: str) -> str:
        # Return cached JSON or None if not found
        return None  # Implement actual Redis or storage logic

    def SetJson(self, cacheKey: str, json: str):
        # Store JSON
        pass  # Implement actual Redis or storage logic

    def Invalidate(self, cacheKey: str):
        # Remove one entry
        pass  # Implement actual Redis or storage logic

    def InvalidateAllForUid(self, uid: str):
        # Remove all entries whose key contains uid
        pass  # Implement actual Redis or storage logic

    def ClearAll(self):
        # Remove everything
        pass  # Implement actual Redis or storage logic
```

```python
from aspose.cells.gridjs import Config

Config.JsonCache.Enable = True
Config.JsonCache.Implementation = RedisJsonCache()
```

When `Implementation` is set, GridJs uses it exclusively and the built-in memory/disk options (`MaxMemoryEntries`, `DiskPath`, and so on) are ignored.

## Performance Results

Measured on the product's own regression tests (a small workbook, repeated `DetailStreamJsonWithUid` calls with the same uid):

- First call (cache miss): full parse + JSON generation time.
- Second call (cache hit): typically **more than 2x faster**, and the benefit grows with workbook size since the JSON is returned without touching the workbook model at all.

## Demo and Examples

For comprehensive implementation examples and detailed usage scenarios, refer to the official demo repository:

https://github.com/aspose-cells/Aspose.Cells.Grid-for-Python-via-.NET/tree/main/Examples.GridJs

## Additional Resources

- [GridJs Server API Documentation](https://reference.aspose.com/cells/python-net/aspose.cellsgridjs)
- [How to Implement Lazy Loading in GridJs](https://docs.aspose.com/cells/python-net/aspose-cells-gridjs/how-to-do-lazy-loading/)
- [GridJs Client API Documentation](https://docs.aspose.com/cells/python-net/aspose-cells-gridjs/how-to-use-gridjs-client-api)