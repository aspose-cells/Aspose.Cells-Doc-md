---
title: Setting Formulas - Notice for Non‑English Users with Go
linktitle: Setting Formulas - Notice for Non‑English Users
type: docs
weight: 10
url: /gocpp/setting-formulas-notice-for-non-english-users/
description: Learn how to set formulas in Aspose.Cells for Go via C with English (US) style for non‑English users.
ai_search_scope: cells_go
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Aspose.Cells supports most of the formulas/functions that are part of Microsoft Excel. Developers can use these formulas with either the API or [designer spreadsheets](/cells/go/what-is-a-designer-spreadsheet/). Aspose.Cells supports a huge set of mathematical, string, Boolean, date/time, statistical, database, lookup, and reference formulas. The formulas should be specified using English (US) style.

{{% /alert %}} 

## **Notice for Non‑English Users**
There are two tips that non‑English users must follow when creating formulas with Aspose.Cells:

1. Formulas must be entered in English. For example, use the English "`=SUM()`" not the German "`=SUMME()`".
2. Always use a comma (,) to delimit function parameters. For some language options or settings, the delimiter for function parameters may be a semicolon, but Aspose.Cells uses the English‑style comma. For example, use "`=IF(C5=0,0,C3/C4)`" not "`=IF(C5=0;0;C3/C4)`".

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingFormulasNoticeForNonEnglishUsers.go" >}}