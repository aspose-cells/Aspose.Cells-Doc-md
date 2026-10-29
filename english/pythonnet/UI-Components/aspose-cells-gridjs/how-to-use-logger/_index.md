---
title: How to Use Logger in GridJs
type: docs
weight: 260
url: /python-net/aspose-cells-gridjs/how-to-use-logger
description: This article explains how to enable and configure the built-in GridJs logger to write diagnostic messages to the console or to log files, with log level filtering and daily/monthly rolling.
keywords: GridJs, logger, logging, GridJsLogger, log level, log file, rolling, diagnostics, troubleshooting
aliases:
  - /python-net/aspose-cells-gridjs/logger/
  - /python-net/aspose-cells-gridjs/logging/
  - /python-net/aspose-cells-gridjs/how-to-configure-logger/

ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## About the GridJs Logger

GridJs ships with a lightweight, built-in logging system: the static class `GridJsLogger` (namespace `aspose.cellsgridjs`). The server components — `GridJsService`, `GridJsWorkbook`, `SimpleHelper` and the default JSON cache — write their diagnostic messages through it, so a single switch controls all GridJs logging in your process.

Key characteristics:

- **Silent by default.** In a Release build the level is `None`, so nothing is written until you configure the logger. In a `DEBUG` build the default level is `Debug`.
- **Two output targets.** Console (stdout/stderr) and a log file. Both can be enabled at the same time.
- **Log level filtering.** Messages below the configured level are discarded.
- **File rolling.** Log files can roll by day or by month, and can additionally roll when a file exceeds a size limit.
- **Global and thread-safe.** Configuration is static (process-wide), and file writes are serialized with a lock, so several concurrent requests can log safely.

## Quick Start

Configure the logger once at application startup — for example in a Flask application factory or app setup block.

### Log to rolling files (recommended for servers)

```python
import aspose.cellsgridjs

# Minimum level to record
aspose.cellsgridjs.GridJsLogger.level = aspose.cellsgridjs.GridJsLogLevel.INFO

# Daily rolling files: gridjs_2026-07-27.log, gridjs_2026-07-28.log, ...
# The directory (and its sub-directories) is created automatically.
aspose.cellsgridjs.GridJsLogger.set_log_directory("/var/logs/gridjs", aspose.cellsgridjs.GridJsLogRolling.DAILY, "gridjs")

# Optional: also rotate when a single file grows beyond 10 MB
aspose.cellsgridjs.GridJsLogger.max_file_size = 10 * 1024 * 1024
```

### Log to the console (useful during development)

```python
aspose.cellsgridjs.GridJsLogger.level = aspose.cellsgridjs.GridJsLogLevel.DEBUG   # output everything
aspose.cellsgridjs.GridJsLogger.enable_console_output = True
```

`Debug`, `Info` and `Warn` messages are written to **stdout**; `Error` messages are written to **stderr**, so they are still visible when standard output is redirected.

### Log to a single file

```python
aspose.cellsgridjs.GridJsLogger.level = aspose.cellsgridjs.GridJsLogLevel.WARN
aspose.cellsgridjs.GridJsLogger.set_log_file("/var/logs/gridjs.log")          # append to the existing file
# aspose.cellsgridjs.GridJsLogger.set_log_file("/var/logs/gridjs.log", False) # overwrite the file on startup
```

`set_log_file` and `set_log_directory` both enable file output automatically. `set_log_file` uses a fixed file name and never rolls, and `max_file_size` is ignored in this mode.

### Turn logging off again

```python
# Cheapest option: keep the configuration, skip all messages
aspose.cellsgridjs.GridJsLogger.level = aspose.cellsgridjs.GridJsLogLevel.NONE

# Or fully close the file writer and reset the path
aspose.cellsgridjs.GridJsLogger.close_log_file()
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
| Single file (via `set_log_file`) | the path you pass | `gridjs.log` |
| `DAILY` | `{prefix}_{yyyy-MM-dd}.log` | `gridjs_2026-07-27.log` |
| `MONTHLY` | `{prefix}_{yyyy-MM}.log` | `gridjs_2026-07.log` |

The default prefix is `gridjs`; pass a different one to `set_log_directory(directory, rolling, file_prefix)`. If the process restarts within the same period, the existing file is appended to rather than overwritten.

When `max_file_size` is greater than `0` and the current file reaches that many bytes, the logger switches to a timestamped file inside the same period:

```text
gridjs_2026-07-27_143512.log
```

The check runs before each write, and the writer is reopened automatically. Setting `max_file_size = 0` (the default) means "no size limit".

> **Note:** Only `DAILY` and `MONTHLY` are currently available; a weekly strategy is reserved and not implemented.

## What GridJs Logs

GridJs itself emits messages under these prefixes:

| Component | Prefix | Typical events |
|-----------|--------|----------------|
| `GridJsService` | `[GridJsService]` | Service instance created/disposed, file or stream import failures, image upload failures. |
| `GridJsWorkbook` | `[GridJsWorkbook]` | Workbook load from file/stream, save failures (`save_to_excel_file`, `save_to_pdf`, `save_to_xlsx`, `save_to_html`), formula calculation errors, batch delete errors, conditional formatting warnings. |
| JSON cache | `[JSON Cache]` | Cache hit/miss, entries stored, disk cache read/write/delete failures. |
| `SimpleHelper` | `[SimpleHelper]` | Picture/shape handling, cache file save failures, address parsing warnings. |

Most `DEBUG` messages describe normal flow (lifecycle, cache hit/miss), `INFO` messages summarize work such as storing a cache entry, `WARN` covers recoverable problems, and `ERROR` marks failures that affect the current request.

## Logging Your Own Messages

Use the same logger for messages from your own controller or service so everything ends up in one place:

```python
aspose.cellsgridjs.GridJsLogger.info("Export started for file " + file_name)
aspose.cellsgridjs.GridJsLogger.debug("Building cache key for uid " + uid)
aspose.cellsgridjs.GridJsLogger.warn("Client requested unknown sheet '" + sheet_name + "'")
aspose.cellsgridjs.GridJsLogger.error("Failed to load workbook: " + str(e))
aspose.cellsgridjs.GridJsLogger.log(aspose.cellsgridjs.GridJsLogLevel.INFO, "Custom message")
```

Because message filtering happens inside `log`, a filtered call still pays the cost of building the string. For expensive messages, guard the call:

```python
if aspose.cellsgridjs.GridJsLogger.level <= aspose.cellsgridjs.GridJsLogLevel.DEBUG:
    aspose.cellsgridjs.GridJsLogger.debug("Workbook dump: " + dump_workbook())
```

## API Reference

| Member | Type | Description |
|--------|------|-------------|
| `level` | `GridJsLogLevel` | Minimum level to record. Default `NONE` (`DEBUG` in DEBUG builds). |
| `enable_console_output` | `bool` | Write to stdout/stderr. Default `false`. |
| `enable_file_output` | `bool` | Write to the log file. Setting it to `true` without a configured path throws `InvalidOperationException`; `set_log_file`/`set_log_directory` enable it for you. |
| `log_file_path` | `str` (read-only) | Path of the file currently being written, or `None` when file output is not configured. |
| `max_file_size` | `int` | Size in bytes at which a rolling file is rotated. `0` (default) means no limit. Ignored in single-file mode. |
| `set_log_file(path)` | `None` | Single file, append mode; enables file output. |
| `set_log_file(path, append)` | `None` | Single file; `append = False` truncates the file. |
| `set_log_directory(dir)` | `None` | Daily rolling with prefix `gridjs`; enables file output. |
| `set_log_directory(dir, rolling)` | `None` | Rolling with the given strategy and prefix `gridjs`. |
| `set_log_directory(dir, rolling, file_prefix)` | `None` | Rolling with the given strategy and file name prefix. |
| `close_log_file()` | `None` | Flushes and closes the writer, disables file output, resets the path and rolling state. |
| `debug/info/warn/error(message)` | `None` | Convenience methods for each level. |
| `log(level, message)` | `None` | Writes a message at an explicit level. |

Enumerations:

- `GridJsLogLevel`: `DEBUG`, `INFO`, `WARN`, `ERROR`, `NONE`.
- `GridJsLogRolling`: `NONE`, `DAILY`, `MONTHLY`.

## Behavior Notes

- **Configure once, process-wide.** The logger is static, so settings apply to every request in the application domain. Configure it at startup, before controllers begin serving requests.
- **The logger never breaks your request.** If the log file cannot be opened, written, closed or rolled, file output is disabled and a `[GridJsLogger] ...` diagnostic is printed to stderr. Logging calls do not throw.
- **File writes are serialized; console output is not.** Concurrent requests can log at the same time: the logger's lock guards the file writer, while console messages go straight through `sys.stdout`, which already synchronizes its own writes.
- **Every line is flushed.** `AutoFlush` is enabled so live logs stay readable, but very chatty `DEBUG` logging on a busy server adds I/O to the request path. Prefer `WARN` or `ERROR` in production.
- **Level filtering is cheap.** When a message is below the threshold, no timestamp, thread ID or formatting is produced; only the caller's string concatenation is wasted.
- **Messages may contain file paths and cache keys.** Log files can reveal server directory structure, so choose a directory with appropriate permissions and retention.

## Recommended Production Settings

```python
aspose.cellsgridjs.GridJsLogger.level = aspose.cellsgridjs.GridJsLogLevel.WARN              # errors and recoverable problems only
aspose.cellsgridjs.GridJsLogger.set_log_directory("/var/logs/gridjs",       # or a Windows path
                                                  aspose.cellsgridjs.GridJsLogRolling.DAILY,
                                                  "gridjs")
aspose.cellsgridjs.GridJsLogger.max_file_size = 20 * 1024 * 1024           # 20 MB per file
aspose.cellsgridjs.GridJsLogger.enable_console_output = False              # keep stdout for the host process
```

Switch to `GridJsLogLevel.DEBUG` temporarily when you need to trace cache behavior, workbook loading or formula calculation; remember to lower it again afterwards.

## Demo and Examples

For comprehensive implementation examples and detailed usage scenarios, refer to the official demo repository:

<https://github.com/aspose-cells/Aspose.Cells.Grid-for-Python-via-.NET/tree/main/Examples.GridJs>

## Additional Resources

- [GridJs Server API Documentation](https://reference.aspose.com/cells/python-net/aspose.cellsgridjs)
- [How to Use JSON Cache Feature in GridJs](https://docs.aspose.com/cells/python-net/aspose-cells-gridjs/how-to-use-json-cache)
- [Settings for GridJs](https://docs.aspose.com/cells/python-net/aspose-cells-gridjs/settings/)