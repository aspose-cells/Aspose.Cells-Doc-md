---
title: How to Use JSON Cache Feature in GridJs  
type: docs
weight: 250
url: /net/aspose-cells-gridjs/how-to-use-json-cache
description: This article describes how to enable and configure the JSON cache feature in GridJs to speed up repeated data requests.
keywords: GridJs, json cache, cache, performance, optimize loading
aliases:
  - /net/aspose-cells-gridjs/jsoncache/
  - /net/aspose-cells-gridjs/json-cache/
  - /net/aspose-cells-gridjs/use-cache/

ai_search_scope: cells_net
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
| `MemoryTtl` | TimeSpan | 1 hour | Lifetime of an in-memory entry. |
| `EnableDisk` | bool | `true` | Whether the disk cache (L2) is used. |
| `DiskPath` | string | `[FileCacheDirectory]/json_cache` | Directory that stores disk cache files. |
| `MaxDiskSizeMB` | long | 500 | Maximum total size of the disk cache; oldest files are deleted beyond this limit. |
| `DiskTtl` | TimeSpan | 24 hours | Lifetime of a disk cache file. |
| `CompressDisk` | bool | `true` | Whether disk cache files are Gzip compressed. |

## Implementation Steps

### Step 1: Enable JSON Cache in Startup.cs

**Example using Config:**

```csharp
Config.JsonCache.Enable = true;
```

**Example using GridJsOptions (ASP.NET Core DI):**

```csharp
services.Configure<GridJsOptions>(options =>
{
    // ... other options
    options.JsonCache.Enable = true;
    options.JsonCache.EnableDisk = true;
    options.JsonCache.DiskPath = @"C:\Temp\gridjs_json_cache"; // optional, defaults to [FileCacheDirectory]/json_cache
    options.JsonCache.MaxMemoryEntries = 1000;
    options.JsonCache.MemoryTtl = TimeSpan.FromHours(1);
    options.JsonCache.MaxDiskSizeMB = 500;
    options.JsonCache.DiskTtl = TimeSpan.FromHours(24);
    options.JsonCache.CompressDisk = true;
});
```

### Step 2: Use the Normal Loading APIs

No client-side change is required. Once the cache is enabled, the `GridJsService` loading APIs check the cache before generating JSON and store the result afterwards:

```csharp
public class GridJs2Controller : Controller
{
    private readonly IGridJsService _service; // registered in DI

    public GridJs2Controller(IGridJsService service)
    {
        _service = service;
    }

    [HttpPost]
    public ActionResult DetailStreamJsonWithUid(string filename, string uid)
    {
        
        string filePath = @"C:\Files\"+filename;

        // First call: cache miss -> JSON is generated and cached
        // Second and later calls with the same uid/file: served directly from cache
        using (GZipStream gzip = new GZipStream(Response.Body, CompressionLevel.Optimal))
        {
            _service.DetailStreamJsonWithUid(gzip, filePath, uid);
        }
        return new EmptyResult();
    }
}
```

### Step 3: Invalidate the Cache When Data Changes

GridJs automatically clears the cached JSON whenever the data is modified through the built-in editing operations of `GridJsService` (`UpdateCell`, image operations, etc.), so stale JSON is never returned to the client.

If you modify the workbook out of band (for example, the file on disk was replaced by your own code), clear the cache explicitly:

```csharp
// Clear all cached entries belonging to one loaded file
_service.ClearJsonCacheForUid(uid);

// Clear every cached entry (memory + disk)
_service.ClearAllJsonCache();
```

## Using a Custom Cache Implementation (Redis, etc.)

If you want to store the JSON in your own infrastructure — for example a distributed Redis cache — implement the `IGridJsJsonCache` interface and assign it to `Implementation`:

```csharp
public class RedisJsonCache : IGridJsJsonCache
{
    public string GetCacheKey(string uid, string fileName)
    {
        // Decide the key strategy:
        // - fileName only -> the same file can share cache across different uids
        // - uid + fileName -> strict isolation per loaded instance
        return string.IsNullOrEmpty(fileName) ? $"gridjs_json_{uid}" : $"gridjs_json_{uid}_{fileName}";
    }

    public string TryGetJson(string cacheKey)   { /* return cached JSON or null */ return null; }
    public void SetJson(string cacheKey, string json) { /* store JSON */ }
    public void Invalidate(string cacheKey)     { /* remove one entry */ }
    public void InvalidateAllForUid(string uid) { /* remove all entries whose key contains uid */ }
    public void ClearAll()                      { /* remove everything */ }
}
```

```csharp
Config.JsonCache.Enable = true;
Config.JsonCache.Implementation = new RedisJsonCache();
```

When `Implementation` is set, GridJs uses it exclusively and the built-in memory/disk options (`MaxMemoryEntries`, `DiskPath`, and so on) are ignored.

## Performance Results

Measured on the product's own regression tests (a small workbook, repeated `DetailStreamJsonWithUid` calls with the same uid):

- First call (cache miss): full parse + JSON generation time.
- Second call (cache hit): typically **more than 2x faster**, and the benefit grows with workbook size since the JSON is returned without touching the workbook model at all.

## Demo and Examples

For comprehensive implementation examples and detailed usage scenarios, refer to the official demo repository:

<https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/tree/main/Examples_GridJs>

## Additional Resources

- [GridJs Server API Documentation](https://reference.aspose.com/cells/net/aspose.cells.gridjs)
- [How to Implement Lazy Loading in GridJs](https://docs.aspose.com/cells/net/aspose-cells-gridjs/how-to-do-lazy-loading/)
- [GridJs Client API Documentation](https://docs.aspose.com/cells/net/aspose-cells-gridjs/how-to-use-gridjs-client-api)
