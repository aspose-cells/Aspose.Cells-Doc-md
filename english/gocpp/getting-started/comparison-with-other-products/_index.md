---
title: Comparison of functionality and performance of Aspose.Cells for Go via C with Excelize, Tealeg/xlsx, and Go-OLE.
type: docs
weight: 40
url: /go-cpp/comparison-of-functionality-and-performance/
description: Comparison of functionality and performance of Aspose.Cells for Go via C with Excelize, Tealeg/xlsx, and Go-OLE.
keywords: Aspose.Cells, Excel, Formula Watch Window, Cells, Adding, C++
---

The following is a comprehensive comparison of Aspose.Cells for Go (via C) with other mainstream Go language Excel processing libraries (Excelize, tealeg/xlsx, go-ole) in terms of functionality, performance, and use cases.

## Differences in basic positioning and structure

| Library Name         |   Type                         | Underlying Implementation          |  CGO Dependency          | Cross-Platform Deployment |
| :------------------- | :----------------------------- | :--------------------------------- | :----------------------- | :-----------------------  |
| Aspose.Cells for Go  | Commercial Library (MIT/Paid)  | Native Engine, Go CGO Wrapper      |  ✅  Yes                 | Support for Windows, Linux |
| Excelize             | Open Source Library (MIT)      | Pure Go Implementation             |  ❌  No                  | Support for Windows, Linux, MacOS |
| tealeg/xlsx          | Open Source Library (BSD)      | Pure Go Implementation             |  ❌  No                  | Support for Windows, Linux, MacOS |
| go-ole               | Open Source Library (BSD)      | Go Windows OLE/COM Interface       |  ✅  Yes (Windows only)  | Windows Only |

### Key differences

- Aspose.Cells for Go via C++ is an industrial-grade commercial library with the most complete functions, but a paid product is required.
- Excelize is currently the most active and open source Go library, pure Go.
- Tealeg/xlsx is an early open source library with more basic functions and slow maintenance.
- Go-ole is a Windows-only COM automation scheme that relies on Excel installation and is not recommend for server environments.

## Feature Comparison

### Supported File Formats Comparison

| Spreadsheet Format     |   Aspose.Cells for Go via C++ | Excelize    | Tealeg/xlsx | Go-OLE (Excel App)    |
| :--------------------- | :---------------------------- | :---------- | :---------- | :-------------------  |
| Xlsx                   | ✅ Yes                        | ✅ Yes     | ✅ Yes       | ✅ Reliant on Excel |
| Xlsb                   | ✅ Yes                        | ❌  No     | ❌  No       | ✅ Reliant on Excel |
| Xls                    | ✅ Yes                        | ❌  No     | ❌  No       | ✅ Reliant on Excel |
| Xlsm                   | ✅ Yes                        | ✅ Yes     | ✅ Yes       | ✅ Reliant on Excel |
| Xltm                   | ✅ Yes                        | ✅ Yes     | ✅ Yes       | ✅ Reliant on Excel |
| Xltx                   | ✅ Yes                        | ✅ Yes     | ✅ Yes       | ✅ Reliant on Excel |
| Csv                    | ✅ Yes                        | ❌  No     | ❌  No       | ✅ Reliant on Excel |
| Ods                    | ✅ Yes                        | ❌  No     | ❌  No       | ✅ Reliant on Excel |
| Html                   | ✅ Yes                        | ❌  No     | ❌  No       | ❌  No              |
| Numbers                | ✅ Yes                        | ❌  No     | ❌  No       | ❌  No              |
| Json                   | ✅ Yes                        | ❌  No     | ❌  No       | ❌  No              |
| Xml                    | ✅ Yes                        | ❌  No     | ❌  No       | ❌  No              |
| SpreadsheetML          | ✅ Yes                        | ❌  No     | ❌  No       | ❌  No              |

### Supported Spreadsheet Features

| Library Features                 |   Aspose.Cells for Go via C++ | Excelize         | Tealeg/xlsx | Go-OLE (Excel App) |
| :----------------------------    | :---------------------------- | :--------------- | :---------- | :----------  |
| Read/Write(Support file format)  | ✅ Yes                        | ✅ Yes          | ✅ Yes     | ✅ Yes   |
| Cell/Row/Column/Worksheet        | ✅ Yes                        | ✅ Yes          | ✅ Yes     | ✅ Yes   |
| Style                            | ✅ Yes                        | ✅ Yes          | ✅ Yes     | ✅ Yes   |
| Formula calculation              | ✅ Yes                        | ✅ Yes (Part)   | ❌  No     | ✅ Yes (calculated by Excel)  |
| Chart/Picture                    | ✅ Yes                        | ✅ Yes (Part)   | ❌  No     | ✅ Yes   |
| PivotTable                       | ✅ Yes                        | ✅ Yes          | ❌  No     | ✅ Yes   |
| Conditional Formatting           | ✅ Yes                        | ✅ Yes          | ❌  No     | ✅ Yes   |
| Data validation                  | ✅ Yes                        | ✅ Yes          | ❌  No     | ✅ Yes   |
| Encryption/password protection   | ✅ Yes                        | ✅ Yes          | ❌  No     | ✅ Yes   |
| Data validation                  | ✅ Yes                        | ✅ Yes          | ❌  No     | ✅ Yes   |
| VBA macro                        | ✅ Yes Read                   | ❌  No          | ❌  No     | ✅ Yes   |
| Data validation                  | ✅ Yes                        | ✅ Yes          | ❌  No     | ✅ Yes   |

## Performance Comparison

Test scenario (assuming a large file, 10 worksheets, 100,000 rows x 250 columns, including formatting):
