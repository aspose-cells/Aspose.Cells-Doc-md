---
title: How to Use Smart Marker Variables and Expressions
linktitle: Variables and Expressions
type: docs
weight: 50
url: /net/smartmarker-variable-expression-usage/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## 1. Why Use This Feature

In traditional SmartMarker usage, data paths, nested mappings, and field concatenation logic are written directly in display cells. For complex multi-level nested JSON data, marker definitions become scattered and difficult to maintain.

Any changes to JSON field names or data hierarchy require modifying markers across multiple cells, resulting in high maintenance costs and a high risk of errors. Repeated field concatenation and combination logic cannot be reused, leading to bloated templates and poor scalability.

To solve these problems, Aspose.Cells provides the **Variables Worksheet** feature. You can create an independent worksheet to uniformly manage data mappings, nested bindings, and custom expressions. It completely separates **data logic from visual layout**, making complex templates cleaner, more maintainable, and support dynamic field calculation.

## 2. Feature Benefits

The Variables Worksheet centralizes variable and expression management, enabling lightweight, reusable, and computable templates. The main advantages are as follows:

- **Centralized variable management**: All nested data paths, raw fields, and concatenation expressions are configured in a dedicated worksheet. The display sheet only focuses on layout, keeping templates clean and organized.

- **Lower maintenance costs**: When data fields or hierarchy changes, you only update the variable configuration, instead of modifying every marker in the entire report.

- **Custom expression calculation**: Supports field concatenation and combination logic in variable definitions. Multiple raw fields can be merged to generate custom business fields without code processing.

- **Global variable reuse**: Defined variables and expressions can be referenced repeatedly across the entire template, ensuring unified rendering rules and avoiding duplicate logic.

- **Separation of logic and style**: The variable worksheet handles data mapping and calculation; the template worksheet handles layout and presentation. This structure is ideal for complex and large-scale report templates.

## 3. How to Use This Feature

The workflow is straightforward: define variables and expressions in the dedicated variables worksheet → reference variables in the template sheet → specify the variable worksheet name in code → render the report automatically.

### 3.1 Template Structure Specification

The template requires two worksheets with clear responsibilities:

- **variables Worksheet**: Stores all hierarchical variable mappings, data bindings, and custom calculation expressions.

- **template Worksheet**: Only references pre-defined variables for layout and display, without writing complex data paths or inline expressions.

### 3.2 Variable Worksheet Configuration Examples

Supports multi-level nested data binding and custom field concatenation expressions:

- Top-level collection mapping: `Directors = RootData.Directors`

- Nested sub-collection mapping: `Reportees = Directors.Reportees`

- Custom concatenation expression: `ReporteeName = {Reportees.FirstName} {Reportees.LastName}`

### 3.3 Template Reference Methods

You can reference defined variables in the display sheet in three ways (recommended methods prioritized):

- Reference raw field directly: `=Reportees.FirstName`

- Reference custom composite variable (Recommended): `=ReporteeName`

- Inline cell concatenation (Not recommended for maintenance): `={Directors.FirstName} &" " &{Reportees.LastName}`

### 3.4 Initialize Template Entirely via Code

You can dynamically generate the complete Excel template in pure C# code, including worksheet creation, variable configuration, expression definition, and SmartMarker binding. No manual Excel editing is required.

```csharp
using Aspose.Cells;
using Aspose.Cells.Markup;

// 1. Initialize a new workbook
Workbook workbook = new Workbook();

// 2. Clear default sheets and create custom worksheets
workbook.Worksheets.Clear();
Worksheet variablesSheet = workbook.Worksheets.Add("variables");
Worksheet templateSheet = workbook.Worksheets.Add("template");

#region 3. Initialize Variables Worksheet (Exact official template structure)
// Table header definition
variablesSheet.Cells["A1"].PutValue("Scope");
variablesSheet.Cells["B1"].PutValue("Name");
variablesSheet.Cells["C1"].PutValue("Variable Name");
variablesSheet.Cells["D1"].PutValue("Variable Value");
variablesSheet.Cells["E1"].PutValue("Type");

// Row 1: Directors variable
variablesSheet.Cells["A2"].PutValue("Worksheet");
variablesSheet.Cells["B2"].PutValue("Template");
variablesSheet.Cells["C2"].PutValue("Directors");
variablesSheet.Cells["D2"].PutValue("RootData.Directors");
variablesSheet.Cells["E2"].PutValue("");

// Row 2: Reportees nested variable
variablesSheet.Cells["A3"].PutValue("Worksheet");
variablesSheet.Cells["B3"].PutValue("Template");
variablesSheet.Cells["C3"].PutValue("Reportees");
variablesSheet.Cells["D3"].PutValue("Directors.Reportees");
variablesSheet.Cells["E3"].PutValue("");

// Row 3: Custom full name expression
variablesSheet.Cells["A4"].PutValue("Worksheet");
variablesSheet.Cells["B4"].PutValue("Template");
variablesSheet.Cells["C4"].PutValue("ReporteeName");
     variablesSheet.Cells["D4"].PutValue("{Reportees.FirstName}&\" \" &{Reportees.LastName}");
variablesSheet.Cells["E4"].PutValue("Expression");
#endregion

#region 4. Initialize Template Display Worksheet (Exact official marker layout)
// Header row
templateSheet.Cells["A1"].PutValue("Directors.FirstName");
templateSheet.Cells["B1"].PutValue("ReporteeName");
templateSheet.Cells["C1"].PutValue("ReporteeName");

// SmartMarker data row
templateSheet.Cells["A2"].PutValue("&=Reportees.FirstName");
templateSheet.Cells["B2"].PutValue("&=ReporteeName");
templateSheet.Cells["C2"].PutValue("&=&={Reportees.FirstName}&\" \" &{Reportees.LastName}");
#endregion

#region 5. Enable Variable Worksheet & Bind JSON Data
WorkbookDesigner designer = new WorkbookDesigner(workbook);
// Enable custom variable worksheet parsing
designer.VariablesWorksheetName = "variables";

// Complete nested JSON source data
string json = @"{
    ""Directors"": [
        {
            ""FirstName"": ""director first 1"",
            ""id"": ""director id 1"",
            ""LastName"": ""director last 1"",
            ""MiddleName"": ""director middle 1"",
            ""Reportees"": [
                {
                    ""City"": ""aaa city"",
                    ""Department"": ""aaa department"",
                    ""FirstName"": ""first aaa"",
                    ""GST"": ""Yes"",
                    ""id"": ""aaa"",
                    ""ITR"": ""No"",
                    ""LastName"": ""last aaa"",
                    ""MiddleName"": ""middle aaa""
                },
                {
                    ""City"": ""bbb city"",
                    ""Department"": ""bbb department"",
                    ""FirstName"": ""first bbb"",
                    ""GST"": ""Yes"",
                    ""id"": ""bbb"",
                    ""ITR"": ""Yes"",
                    ""LastName"": ""last bbb"",
                    ""MiddleName"": ""middle bbb""
                },
                {
                    ""City"": ""ccc city"",
                    ""Department"": ""ccc department"",
                    ""FirstName"": ""first ccc"",
                    ""GST"": ""No"",
                    ""id"": ""ccc"",
                    ""ITR"": ""No"",
                    ""LastName"": ""last ccc"",
                    ""MiddleName"": ""middle ccc""
                }
            ]
        },
        {
            ""FirstName"": ""director first 2"",
            ""id"": ""director id 2"",
            ""LastName"": ""director last 2"",
            ""MiddleName"": ""director middle 2"",
            ""Reportees"": [
                {
                    ""City"": ""eee city"",
                    ""Department"": ""eee department"",
                    ""FirstName"": ""first eee"",
                    ""GST"": ""Yes"",
                    ""id"": ""eee"",
                    ""ITR"": ""No"",
                    ""LastName"": ""last eee"",
                    ""MiddleName"": ""middle eee""
                },
                {
                    ""City"": ""fff city"",
                    ""Department"": ""fff department"",
                    ""FirstName"": ""first fff"",
                    ""GST"": ""No"",
                    ""id"": ""fff"",
                    ""ITR"": ""No"",
                    ""LastName"": ""last fff"",
                    ""MiddleName"": ""middle fff""
                }
            ]
        }
    ],
    ""DOB"": ""2025-02-08"",
    ""EntityCin"": ""EntityCin Test"",
    ""EntityName"": ""EntityName Test"",
    ""FirstName"": ""FirstName Test"",
    ""LastName"": ""LastName Test"",
    ""MiddleName"": ""MiddleName Test"",
    ""SSN"": ""11111111""
}";

// Bind data source and process markers
designer.SetDataSource("RootData", json);
designer.Process();
#endregion

// 6. Export final generated report
workbook.Save("SmartMarker_Variable_Expression_Template.xlsx");

```


