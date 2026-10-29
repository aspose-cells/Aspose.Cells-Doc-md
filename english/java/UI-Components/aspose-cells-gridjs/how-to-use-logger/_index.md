---
title: How to Use Logger in GridJs
type: docs
weight: 260
url: /java/aspose-cells-gridjs/how-to-use-logger
description: This article explains how to enable and configure the built-in GridJs logger to write diagnostic messages to the console or to log files, with log level filtering and daily/monthly rolling.
keywords: GridJs, logger, logging, GridJsLogger, log level, log file, rolling, diagnostics, troubleshooting
aliases:
  - /java/aspose-cells-gridjs/logger/
  - /java/aspose-cells-gridjs/logging/
  - /java/aspose-cells-gridjs/how-to-configure-logger/

ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## About the GridJs Logger

GridJs ships with a lightweight, built-in logging system: the static class `GridJsLogger` (package `com.aspose.gridjs`). The server components — `GridJsService`, `GridJsWorkbook`, `SimpleHelper` and the default JSON cache — write their diagnostic messages through it, so a single switch controls all GridJs logging in your process.

Key characteristics:

- **Silent by default.** In a Release build the level is `None`, so nothing is written until you configure the logger. In a `DEBUG` build the default level is `Debug`.
- **Two output targets.** Console (stdout/stderr) and a log file. Both can be enabled at the same time.
- **Log level filtering.** Messages below the configured level are discarded.
- **File rolling.** Log files can roll by day or by month, and can additionally roll when a file exceeds a size limit.
- **Global and thread-safe.** Configuration is static (process-wide), and file writes are serialized with a lock, so several concurrent requests can log safely.

## Quick Start

Configure the logger once at application startup — for example in your main application class or Spring configuration.

### Log to rolling files (recommended for servers)

```java
import com.aspose.gridjs.GridJsLogLevel;
import com.aspose.gridjs.GridJsLogRolling;
import com.aspose.gridjs.GridJsLogger;

// Minimum level to record
GridJsLogger.setLevel(GridJsLogLevel.INFO);

// Daily rolling files: gridjs_2026-07-27.log, gridjs_2026-07-28.log, ...
// The directory (and its sub-directories) is created automatically.
GridJsLogger.setLogDirectory("/var/log/gridjs", GridJsLogRolling.DAILY, "gridjs");

// Optional: also rotate when a single file grows beyond 10 MB
GridJsLogger.setMaxFileSize(10 * 1024 * 1024);
```

### Log to the console (useful during development)

```java
GridJsLogger.setLevel(GridJsLogLevel.DEBUG);   // output everything
GridJsLogger.setEnableConsoleOutput(true);
```

`Debug`, `Info` and `Warn` messages are written to **stdout**; `Error` messages are written to **stderr**, so they are still visible when standard output is redirected.

### Log to a single file

```java
GridJsLogger.setLevel(GridJsLogLevel.WARN);
GridJsLogger.setLogFile("/var/log/gridjs.log");          // append to the existing file
// GridJsLogger.setLogFile("/var/log/gridjs.log", false); // overwrite the file on startup
```

`setLogFile` and `setLogDirectory` both enable file output automatically. `setLogFile` uses a fixed file name and never rolls, and `setMaxFileSize` is ignored in this mode.

### Turn logging off again

```java
// Cheapest option: keep the configuration, skip all messages
GridJsLogger.setLevel(GridJsLogLevel.NONE);

// Or fully close the file writer and reset the path
GridJsLogger.closeLogFile();
```

## Log Levels

`GridJsLogLevel` is ordered, and the level you set is the **minimum** that gets recorded:

| Level | Value | Records |
|-------|-------|---------|
| `DEBUG` | 0 | Everything, including per-request details such as cache hit/miss and instance lifecycle. Equivalent to "all". |
| `INFO` | 1 | `INFO`, `WARN`, `ERROR`. |
| `WARN` | 2 | `WARN`, `ERROR`. |
| `ERROR` | 3 | `ERROR` only. |
| `NONE` | 4 | Nothing. This is the default in Release builds. |

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
| Single file (via `setLogFile`) | the path you pass | `gridjs.log` |
| `DAILY` | `{prefix}_{yyyy-MM-dd}.log` | `gridjs_2026-07-27.log` |
| `MONTHLY` | `{prefix}_{yyyy-MM}.log` | `gridjs_2026-07.log` |

The default prefix is `gridjs`; pass a different one to `setLogDirectory(directory, rolling, filePrefix)`. If the process restarts within the same period, the existing file is appended to rather than overwritten.

When `setMaxFileSize` is greater than `0` and the current file reaches that many bytes, the logger switches to a timestamped file inside the same period:

```text
gridjs_2026-07-27_143512.log
```

The check runs before each write, and the writer is reopened automatically. Setting `setMaxFileSize = 0` (the default) means "no size limit".

> **Note:** Only `DAILY` and `MONTHLY` are currently available; a weekly strategy is reserved and not implemented.

## What GridJs Logs

GridJs itself emits messages under these prefixes:

| Component | Prefix | Typical events |
|-----------|--------|----------------|
| `GridJsService` | `[GridJsService]` | Service instance created/disposed, file or stream import failures, image upload failures. |
| `GridJsWorkbook` | `[GridJsWorkbook]` | Workbook load from file/stream, save failures (`saveToExcelFile`, `saveToPdf`, `saveToXlsx`, `saveToHtml`), formula calculation errors, batch delete errors, conditional formatting warnings. |
| JSON cache | `[JSON Cache]` | Cache hit/miss, entries stored, disk cache read/write/delete failures. |
| `SimpleHelper` | `[SimpleHelper]` | Picture/shape handling, cache file save failures, address parsing warnings. |

Most `DEBUG` messages describe normal flow (lifecycle, cache hit/miss), `INFO` messages summarize work such as storing a cache entry, `WARN` covers recoverable problems, and `ERROR` marks failures that affect the current request.

## Logging Your Own Messages

Use the same logger for messages from your own controller or service so everything ends up in one place:

```java
GridJsLogger.info("Export started for file " + fileName);
GridJsLogger.debug("Building cache key for uid " + uid);
GridJsLogger.warn("Client requested unknown sheet '" + sheetName + "'");
GridJsLogger.error("Failed to load workbook: " + ex.getMessage());
GridJsLogger.log(GridJsLogLevel.INFO, "Custom message");
```

Because message filtering happens inside `log`, a filtered call still pays the cost of building the string. For expensive messages, guard the call:

```java
if (GridJsLogger.getLevel() <= GridJsLogLevel.DEBUG) {
    GridJsLogger.debug("Workbook dump: " + dumpWorkbook());
}
```

## API Reference

| Member | Type | Description |
|--------|------|-------------|
| `getLevel()` / `setLevel(value)` | `GridJsLogLevel` | Minimum level to record. Default `NONE` (`DEBUG` in DEBUG builds). |
| `getEnableConsoleOutput()` / `setEnableConsoleOutput(value)` | `boolean` | Write to stdout/stderr. Default `false`. |
| `getEnableFileOutput()` / `setEnableFileOutput(value)` | `boolean` | Write to the log file. Setting it to `true` without a configured path throws `InvalidOperationException`; `setLogFile`/`setLogDirectory` enable it for you. |
| `getLogFilePath()` | `String` (read-only) | Path of the file currently being written, or `null` when file output is not configured. |
| `getMaxFileSize()` / `setMaxFileSize(value)` | `long` | Size in bytes at which a rolling file is rotated. `0` (default) means no limit. Ignored in single-file mode. |
| `setLogFile(path)` | `void` | Single file, append mode; enables file output. |
| `setLogFile(path, append)` | `void` | Single file; `append = false` truncates the file. |
| `setLogDirectory(dir)` | `void` | Daily rolling with prefix `gridjs`; enables file output. |
| `setLogDirectory(dir, rolling)` | `void` | Rolling with the given strategy and prefix `gridjs`. |
| `setLogDirectory(dir, rolling, prefix)` | `void` | Rolling with the given strategy and file name prefix. |
| `closeLogFile()` | `void` | Flushes and closes the writer, disables file output, resets the path and rolling state. |
| `debug(message)` / `info(message)` / `warn(message)` / `error(message)` | `void` | Convenience methods for each level. |
| `log(level, message)` | `void` | Writes a message at an explicit level. |

Enumerations:

- `GridJsLogLevel`: `DEBUG`, `INFO`, `WARN`, `ERROR`, `NONE`.
- `GridJsLogRolling`: `NONE`, `DAILY`, `MONTHLY`.

## Behavior Notes

- **Configure once, process-wide.** The logger is static, so settings apply to every request in the application domain. Configure it at startup, before controllers begin serving requests.
- **The logger never breaks your request.** If the log file cannot be opened, written, closed or rolled, file output is disabled and a `[GridJsLogger] ...` diagnostic is printed to stderr. Logging calls do not throw.
- **File writes are serialized; console output is not.** Concurrent requests can log at the same time: the logger's lock guards the file writer, while console messages go straight through `System.out`, which already synchronizes its own writes.
- **Every line is flushed.** `AutoFlush` is enabled so live logs stay readable, but very chatty `DEBUG` logging on a busy server adds I/O to the request path. Prefer `WARN` or `ERROR` in production.
- **Level filtering is cheap.** When a message is below the threshold, no timestamp, thread ID or formatting is produced; only the caller's string concatenation is wasted.
- **Messages may contain file paths and cache keys.** Log files can reveal server directory structure, so choose a directory with appropriate permissions and retention.

## Recommended Production Settings

```java
GridJsLogger.setLevel(GridJsLogLevel.WARN);              // errors and recoverable problems only
GridJsLogger.setLogDirectory("/var/log/gridjs",       // or a Windows path
                             GridJsLogRolling.DAILY,
                             "gridjs");
GridJsLogger.setMaxFileSize(20 * 1024 * 1024);           // 20 MB per file
GridJsLogger.setEnableConsoleOutput(false);              // keep stdout for the host process
```

Switch to `GridJsLogLevel.DEBUG` temporarily when you need to trace cache behavior, workbook loading or formula calculation; remember to lower it again afterwards.

## Demo and Examples

For comprehensive implementation examples and detailed usage scenarios, refer to the official demo repository:

<https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/main/Examples.GridJs>

## Additional Resources

- [GridJs Server API Documentation](https://reference.aspose.com/cells/java/com.aspose.gridjs)
- [How to Use JSON Cache Feature in GridJs](https://docs.aspose.com/cells/java/aspose-cells-gridjs/how-to-use-json-cache)
- [Settings for GridJs](https://docs.aspose.com/cells/java/aspose-cells-gridjs/settings/)