---
title: Set a Table's Hide Attributes from the Modify Attribute Form
type: docs
weight: 10
aliases: [/reportingservices/set-a-table-s-hide-attributes-from-the-modify-attribute-form/]
url: /reportingservices/set-a-table-hide-attributes-from-the-modify-attribute-form/
ai_search_scope: cells_reportingservices
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Overview  

This article explains how to hide a **table**, **row**, or **column** in a table report by using the **Modify Attribute** form of Aspose.Cells Reporting Services.

## Parameters  

| Parameter | Type    | Required | Description                                                                                           |
|-----------|---------|----------|-------------------------------------------------------------------------------------------------------|
| **type**  | string  | Yes      | The kind of object to hide. Allowed values:  `table`, `row`, `column`.                                 |
| **index** | integer | Yes      | Zero‑based position of the object to hide. Omitted (or `null`) when `type` is `worksheet`.           |
| **expression** | string | Yes | The hide state. Use `true`/`false` or a valid Excel formula (e.g., `=A1>10`). Supports Reporting Services formulas. |

\*If `type` is `row` or `column`, `index` must be supplied. For `table`, the index is always `0`.

## Visual Guide - Setting a table report's hide attributes

![Modify Attribute form – setting hide attributes for a table](set-a-table-hide-attributes-from-the-modify-attribute-form_1.png)
