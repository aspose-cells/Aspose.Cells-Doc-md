---
title: How to use date picker
description: Use the GridJs date picker to select dates in the editor, including year/month
  switching and date range restrictions.
keywords: Datepicker, Calendar, minDate, maxDate, defaultViewDate, date validation,
  date format
type: docs
weight: 1
url: /python-net/aspose-cells-gridjs/user-guide/how-to-use-date-picker/
---

## Introduction

GridJs includes a `Datepicker` component in the cell editor (`component/datepicker.js`).

The date picker uses `Calendar` (`component/calendar.js`) and supports three view modes in code: `date`, `month`, and `year`. The editor can apply global datepicker options from `data.settings.datepicker` and can also merge limits from date validation rules (`component/editor.js`).

## How to use

1. Select a cell and open the editor.

2. Use a date-formatted or date-detected cell.

   In `Editor.setCell(...)`, GridJs calls `prepareDatepicker(...)` when one of these conditions is true:
   - `style.format === 'date'`
   - `data.isDate(text)`
   - `data.isDateFormat(style.custom)`
   - `validator.type === 'date'`
   - date validation is detected by `isDateValidation(...)`

3. Configure date range and default view in initialization options when needed.

   The editor reads `data.settings.datepicker` and normalizes:
   - `minDate`
   - `maxDate`
   - `defaultViewDate`

   `Calendar` disables out-of-range items in day/month/year views through:
   - `isDateDisabled(...)`
   - `isMonthDisabled(...)`
   - `isYearDisabled(...)`

4. Click year/month title to switch views.

   In `Calendar`, the year and month title buttons call:
   - `showYearView()`
   - `showMonthView()`

   Year selection enters month view, and month selection returns to date view.

5. Select a day.

   `Datepicker.change(...)` is wired in `Editor` to call `this.setText(dateFormat(d))`. The saved text format is `yyyy-mm-dd`.

## JavaScript API

The inspected code does not expose a dedicated public API for opening the date picker directly. Behavior is driven by editor flow and options.

### Relevant functions
| Function / Location | Description | Parameters | Returns |
|----------|-------------|------------|---------|
| `Datepicker` (`component/datepicker.js`) | Creates datepicker and delegates date rendering to `Calendar`. | `options` | `Datepicker` instance |
| `Calendar.setOptions(options)` (`component/calendar.js`) | Applies normalized `minDate`, `maxDate`, `defaultViewDate`. | `options` | `void` |
| `Calendar.showYearView()` / `showMonthView()` (`component/calendar.js`) | Switches view mode for year/month selection. | None | `void` |
| `Calendar.buildDateBody()` (`component/calendar.js`) | Builds day grid and handles day click selection. | None | `void` |
| `buildDatepickerOptions(...)` (`component/editor.js`) | Merges global settings and validation-based date limits/default view. | `data`, `validator`, `validation`, `text` | `options` object |
| `prepareDatepicker(...)` (`component/editor.js`) | Applies options, shows datepicker, and sets initial value/view date. | `datepicker`, `text`, `textEl`, `data`, `validator`, `validation` | `void` |

## Common Questions

Q: How is `defaultViewDate` chosen when multiple sources exist?
A: `buildDatepickerOptions(...)` first merges global options and validation options, then prefers parsed cell text date; if text is empty and no default is set, it falls back to `minDate` or `maxDate`.

Q: How are validation limits merged with global options?
A: `mergeDatepickerOptions(...)` normalizes both sources and uses `chooseMinDate(...)` / `chooseMaxDate(...)` so stricter bounds can override looser bounds.

Q: Which views enforce range limits?
A: All three views enforce limits in code: day (`isDateDisabled`), month (`isMonthDisabled`), and year (`isYearDisabled`).

Q: What value is written after picking a date?
A: `Editor` formats selected date through `dateFormat(d)` and writes `yyyy-mm-dd`.
