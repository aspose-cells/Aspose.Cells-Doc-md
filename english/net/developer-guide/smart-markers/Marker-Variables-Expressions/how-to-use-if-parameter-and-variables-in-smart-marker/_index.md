---
title: How to Use If Parameter and Variables in SmartMarkers
type: docs
weight: 100
url: /net/how-to-use-if-parameter-and-Variables-in-smart-markers/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

# How to Use SmartMarker IF Variable Conditions to Filter Data

## 1\. Feature Overview

SmartMarker supports dynamic data filtering through **IF conditions** to control whether row data is rendered in reports\. This feature fully supports two standard IF condition methods: direct field expression writing and boolean variable writing defined in the variable worksheet\. Users can reference boolean expression variables preset in the variable worksheet directly in IF judgments\.

Users can either write filter expressions directly in cells or encapsulate complex range judgments, status checks, and multi\-condition combination logic into global variables for reuse in templates, effectively organizing scattered conditional logic and simplifying the maintenance of complex report templates\.

## 2\. Feature Benefits

IF variable condition filtering optimizes the data filtering capability of SmartMarker, bringing the following core advantages:

- **Unified conditional logic management**: All data filtering rules, boolean judgments and range checks are centrally configured in the variable worksheet, instead of being scattered in display cells\.

- **Global reuse of filter rules**: Defined boolean condition variables can be referenced repeatedly across the entire report template without rewriting complex expressions\.

- **Lower maintenance costs**: When business filter rules change, only the variable worksheet configuration needs to be updated, without modifying template markers in batches\.

- **Support for complex combined conditions**: Custom multi\-field and multi\-logic composite judgments are supported, and variables can be nested in AND / OR logical functions\.

- **Cleaner template structure**: Display cells only reference variable names without lengthy judgment expressions, making templates neat and readable\.

## 3\. Usage Guide

General workflow: Define boolean condition variables in the variable worksheet → Reference variables through IF conditions in template cells → Enable the variable worksheet and render with code\.

### 3\.1 Variable Worksheet Configuration Rules

In the independent variables worksheet, define all data filtering logic as**expression\-type variables**, supporting single\-condition judgment and complex multi\-field combined judgment\.

|Scope|Name|Variable Name|Variable Value|Type|
|---|---|---|---|---|
|Worksheet|Template|booksUpto100Check|\{node\.books\.price\} \&lt;= 100|Expression|
|Worksheet|Template|booksAbove200Check|\{node\.books\.price\} \&gt; 200|Expression|
|Worksheet|Template|bookAvailable|\{node\.books\.isAvailable\} = true|Expression|

### 3\.2 Template Marker Syntax

SmartMarker IF conditions support multiple standard syntaxes\. You can use direct field expressions or reference pre\-defined boolean variables and composite logic variables in the variable worksheet to adapt to different template development scenarios\.

- **1\. Field Expression Condition**

Marker Syntax: `\&amp;=node\.books\.price\(if:\{node\.books\.price\} \&lt;= 100\)`

Marker Syntax: `\&amp;=bookPrice\(if:\{bookPrice\} \&lt;= 100\)`

Function: Write complete field judgment expressions directly in IF parameters to implement data filtering\.

- **2\. Boolean Variable Condition**

Marker Syntax: `\&amp;=node\.books\.price\(if:\{booksUpto100Check\}\)`

Function: Reference pre\-defined boolean expression variables in the variable worksheet to reuse conditional logic and simplify template markers\.

- **3\. Direct Boolean Variable Output**

Marker Syntax: `\&amp;=\{booksUpto100\}`

Marker Syntax: `\&amp;=booksUpto100`

Function: Directly render boolean variable results to display conditional judgment values\.

- **4\. Multi\-Variable Combined Condition**

Marker Syntax: `\&amp;=node\.books\.price\(if:AND\(\{bookAvailable\},\{booksAbove200Check\}\)\)`

Function: Combine multiple boolean variables with AND/OR logical functions to implement complex multi\-condition data filtering\.

### 3\.3 Core Implementation Code

Specify the variable worksheet name to enable variable parsing, allowing SmartMarker to recognize custom boolean variables in IF conditions correctly\.

## 4\. Important Notes

- **Exact Worksheet Name Matching**: The name assigned to `VariablesWorksheetName` must strictly match the name of the custom variable worksheet\. Otherwise, the engine cannot resolve custom boolean variables in IF conditions\.

- **Valid Boolean Expression Definition**: Variables used in IF conditions must return standard boolean results \(true/false\)\. Ensure the configured expression logic is complete and correct to avoid empty or incorrect filtering results\.

- **Standard Logical Function Usage**: When combining multiple variables with `AND\(\)` or `OR\(\)`, all parameters inside the function must be valid boolean variables or boolean expressions to ensure normal parsing\.

- **Correct Variable Reference Syntax**: When referencing variables in IF parameters, use the standard format `if:\{variableName\}`\. Missing braces or incorrect variable names will lead to parsing failure\.

- **Unified Data Source Prefix**: The field prefix defined in the variable expression must be consistent with the root data source name bound by `SetDataSource`, preventing field resolution errors caused by inconsistent data source paths\.
