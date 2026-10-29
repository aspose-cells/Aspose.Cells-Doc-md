---
title: How to Use Logger in GridJs
type: docs
weight: 260
url: /net/aspose-cells-gridjs/how-to-use-logger
description: This article explains how to enable and configure the built-in GridJs logger to write diagnostic messages to the console or to log files, with log level filtering and daily/monthly rolling.
keywords: GridJs, logger, logging, GridJsLogger, log level, log file, rolling, diagnostics, troubleshooting
aliases:
  - /net/aspose-cells-gridjs/logger/
  - /net/aspose-cells-gridjs/logging/
  - /net/aspose-cells-gridjs/how-to-configure-logger/

ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## About the GridJs Logger

GridJs ships with a lightweight, built-in logging system: the static class `GridJsLogger` (namespace `Aspose.Cells.GridJs`). The server components — `GridJsService`, `GridJsWorkbook`, `SimpleHelper` and the default JSON cache — write their diagnostic messages through it, so a single switch controls all GridJs logging in your process.

Key characteristics:

- **Silent by default.** In a Release build the level is `None`, so nothing is written until you configure the logger. In a `DEBUG` build the default level is `Debug`.
- **Two output targets.** Console (stdout/stderr) and a log file. Both can be enabled at the same time.
- **Log level filtering.** Messages below the configured level are discarded.
- **File rolling.** Log files can roll by day or by month, and can additionally roll when a file exceeds a size limit.
- **Global and thread-safe.** Configuration is static (process-wide), and file writes are serialized with a lock, so several concurrent requests can log safely.

## Quick Start

Configure the logger once at application startup — for example in `Program.cs` or `Startup.cs`.

### Log to rolling files (recommended for servers)

```csharp
using Aspose.Cells.GridJs;

// Minimum level to record
GridJsLogger.Level = GridJsLogLevel.Info;

// Daily rolling files: gridjs_2026-07-27.log, gridjs_2026-07-28.log, ...
// The directory (and its sub-directories) is created automatically.
GridJsLogger.SetLogDirectory(@"C:\Logs\gridjs", GridJsLogRolling.Daily, "gridjs");

// Optional: also rotate when a single file grows beyond 10 MB
GridJsLogger.MaxFileSize = 10 * 1024 * 1024;
```

### Log to the console (useful during development)

```csharp
GridJsLogger.Level = GridJsLogLevel.Debug;   // output everything
GridJsLogger.EnableConsoleOutput = true;
```

`Debug`, `Info` and `Warn` messages are written to **stdout**; `Error` messages are written to **stderr**, so they are still visible when standard output is redirected.

### Log to a single file

```csharp
GridJsLogger.Level = GridJsLogLevel.Warn;
GridJsLogger.SetLogFile(@"C:\Logs\gridjs.log");          // append to the existing file
// GridJsLogger.SetLogFile(@"C:\Logs\gridjs.log", false); // overwrite the file on startup
```

`SetLogFile` and `SetLogDirectory` both enable file output automatically. `SetLogFile` uses a fixed file name and never rolls, and `MaxFileSize` is ignored in this mode.

### Turn logging off again

```csharp
// Cheapest option: keep the configuration, skip all messages
GridJsLogger.Level = GridJsLogLevel.None;

// Or fully close the file writer and reset the path
GridJsLogger.CloseLogFile();
```

## Log Levels

`GridJsLogLevel` is ordered, and the level you set is the **minimum** that gets recorded:

| Level | Value | Records |
|-------|-------|---------|
| `Debug` | 0 | Everything, including per-request details such as cache hit/miss and instance lifecycle. Equivalent to "all". |
| `Info` | 1 | `Info`, `Warn`, `Error`. |
| `Warn` | 2 | `Warn`, `Error`. |
| `Error` | 3 | `Error` only. |
| `None` | 4 | Nothing. This is the default in Release builds. |

## Log Line Format

Every message is written as a single line:

```text
[yyyy-MM-dd HH:mm:ss.fff] [LEVEL] [Thread-N] message
```

For example:

```text
[2026-07-27 14:35:12.345] [INFO ] [Thread-7] [JSON Cache] Stored in LazyLoadingJson cache: gridjs_json_ab12_Book1.xlsx_Sheet1, size=24817 chars
[2026-07-27 14:35:12.401] [WARN ] [Thread-9] [GridJsWorkbook] Failed to parse CellArea from 'A1:'
[2026-07-27 14:35:13.020] [ERROR] [Thread-7] [GridJsService] ImportExcelFile from path 'C:\Files\Book1.xlsx' error: Invalid file format.
```

- The timestamp is local time with millisecond precision.
- The level is padded to five characters so columns line up.
- `Thread-N` is the managed thread ID of the thread that produced the message — useful for tracing concurrent requests.
- Files are written in UTF-8 and flushed after every line, so the log is readable while the application is running.

## Log File Rolling

`GridJsLogRolling` selects the rolling strategy:

| Strategy | File name | Example |
|----------|-----------|---------|
| Single file (via `SetLogFile`) | the path you pass | `gridjs.log` |
| `Daily` | `{prefix}_{yyyy-MM-dd}.log` | `gridjs_2026-07-27.log` |
| `Monthly` | `{prefix}_{yyyy-MM}.log` | `gridjs_2026-07.log` |

The default prefix is `gridjs`; pass a different one to `SetLogDirectory(directory, rolling, filePrefix)`. If the process restarts within the same period, the existing file is appended to rather than overwritten.

When `MaxFileSize` is greater than `0` and the current file reaches that many bytes, the logger switches to a timestamped file inside the same period:

```text
gridjs_2026-07-27_143512.log
```

The check runs before each write, and the writer is reopened automatically. Setting `MaxFileSize = 0` (the default) means "no size limit".

> **Note:** Only `Daily` and `Monthly` are currently available; a weekly strategy is reserved and not implemented.

## What GridJs Logs

GridJs itself emits messages under these prefixes:

| Component | Prefix | Typical events |
|-----------|--------|----------------|
| `GridJsService` | `[GridJsService]` | Service instance created/disposed, file or stream import failures, image upload failures. |
| `GridJsWorkbook` | `[GridJsWorkbook]` | Workbook load from file/stream, save failures (`SaveToExcelFile`, `SaveToPdf`, `SaveToXlsx`, `SaveToHtml`), formula calculation errors, batch delete errors, conditional formatting warnings. |
| JSON cache | `[JSON Cache]` | Cache hit/miss, entries stored, disk cache read/write/delete failures. |
| `SimpleHelper` | `[SimpleHelper]` | Picture/shape handling, cache file save failures, address parsing warnings. |

Most `Debug` messages describe normal flow (lifecycle, cache hit/miss), `Info` messages summarize work such as storing a cache entry, `Warn` covers recoverable problems, and `Error` marks failures that affect the current request.

## Logging Your Own Messages

Use the same logger for messages from your own controller or service so everything ends up in one place:

```csharp
GridJsLogger.Info("Export started for file " + fileName);
GridJsLogger.Debug("Building cache key for uid " + uid);
GridJsLogger.Warn("Client requested unknown sheet '" + sheetName + "'");
GridJsLogger.Error("Failed to load workbook: " + ex.Message);
GridJsLogger.Log(GridJsLogLevel.Info, "Custom message");
```

Because message filtering happens inside `Log`, a filtered call still pays the cost of building the string. For expensive messages, guard the call:

```csharp
if (GridJsLogger.Level <= GridJsLogLevel.Debug)
{
    GridJsLogger.Debug("Workbook dump: " + DumpWorkbook());
}
```

## API Reference

| Member | Type | Description |
|--------|------|-------------|
| `Level` | `GridJsLogLevel` | Minimum level to record. Default `None` (`Debug` in DEBUG builds). |
| `EnableConsoleOutput` | `bool` | Write to stdout/stderr. Default `false`. |
| `EnableFileOutput` | `bool` | Write to the log file. Setting it to `true` without a configured path throws `InvalidOperationException`; `SetLogFile`/`SetLogDirectory` enable it for you. |
| `LogFilePath` | `string` (read-only) | Path of the file currently being written, or `null` when file output is not configured. |
| `MaxFileSize` | `long` | Size in bytes at which a rolling file is rotated. `0` (default) means no limit. Ignored in single-file mode. |
| `SetLogFile(path)` | `void` | Single file, append mode; enables file output. |
| `SetLogFile(path, append)` | `void` | Single file; `append = false` truncates the file. |
| `SetLogDirectory(dir)` | `void` | Daily rolling with prefix `gridjs`; enables file output. |
| `SetLogDirectory(dir, rolling)` | `void` | Rolling with the given strategy and prefix `gridjs`. |
| `SetLogDirectory(dir, rolling, prefix)` | `void` | Rolling with the given strategy and file name prefix. |
| `CloseLogFile()` | `void` | Flushes and closes the writer, disables file output, resets the path and rolling state. |
| `Debug/Info/Warn/Error(message)` | `void` | Convenience methods for each level. |
| `Log(level, message)` | `void` | Writes a message at an explicit level. |

Enumerations:

- `GridJsLogLevel`: `Debug`, `Info`, `Warn`, `Error`, `None`.
- `GridJsLogRolling`: `None`, `Daily`, `Monthly`.

## Behavior Notes

- **Configure once, process-wide.** The logger is static, so settings apply to every request in the application domain. Configure it at startup, before controllers begin serving requests.
- **The logger never breaks your request.** If the log file cannot be opened, written, closed or rolled, file output is disabled and a `[GridJsLogger] ...` diagnostic is printed to stderr. Logging calls do not throw.
- **File writes are serialized; console output is not.** Concurrent requests can log at the same time: the logger's lock guards the file writer, while console messages go straight through `Console`, which already synchronizes its own writes.
- **Every line is flushed.** `AutoFlush` is enabled so live logs stay readable, but very chatty `Debug` logging on a busy server adds I/O to the request path. Prefer `Warn` or `Error` in production.
- **Level filtering is cheap.** When a message is below the threshold, no timestamp, thread ID or formatting is produced; only the caller's string concatenation is wasted.
- **Messages may contain file paths and cache keys.** Log files can reveal server directory structure, so choose a directory with appropriate permissions and retention.

## Recommended Production Settings

```csharp
GridJsLogger.Level = GridJsLogLevel.Warn;              // errors and recoverable problems only
GridJsLogger.SetLogDirectory(@"/var/log/gridjs",       // or a Windows path
                             GridJsLogRolling.Daily,
                             "gridjs");
GridJsLogger.MaxFileSize = 20 * 1024 * 1024;           // 20 MB per file
GridJsLogger.EnableConsoleOutput = false;              // keep stdout for the host process
```

Switch to `GridJsLogLevel.Debug` temporarily when you need to trace cache behavior, workbook loading or formula calculation; remember to lower it again afterwards.

## Demo and Examples

For comprehensive implementation examples and detailed usage scenarios, refer to the official demo repository:

<https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/tree/main/Examples_GridJs>

## Additional Resources

- [GridJs Server API Documentation](https://reference.aspose.com/cells/net/aspose.cells.gridjs)
- [How to Use JSON Cache Feature in GridJs](https://docs.aspose.com/cells/net/aspose-cells-gridjs/how-to-use-json-cache)
- [Settings for GridJs](https://docs.aspose.com/cells/net/aspose-cells-gridjs/settings/)
