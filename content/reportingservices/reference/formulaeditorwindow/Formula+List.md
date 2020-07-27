+++
title = "Formula List" 
description = "" 
weight = 12095 
+++

Aspose.Cells for Reporting Services : Formula List  

# Aspose.Cells for Reporting Services : Formula List


### Report fields

{{< table style="table-striped" >}}
|**Set Name**|**Formula Name**|**Description**|
|:----|:----|:----|
|Global fields|ExecutionTime|The date and time when the report began to run.|
| |ReportServerUrl|The URL of the report server on which the report is being run.|
| |ReportName|The name of the report as it is stored in the report server database.|
| |ReportFolder|The full path to the folder containing the report. This does not include the report server URL.|
|User|UserID|The ID of the user running the report.|
| |Language|The language ID of the user running the report.|
{{< /table >}}

### Report fields

{{< table style="table-striped" >}}
|**Set Name**|**Description**|
|:----|:----|
|Parameters|The Parameters collection contains the report parameters within the report. Parameters can be passed to queries, used in filters or used in other functions that alter the report appearance based on the parameter.|
|Fields|The Fields collection contains the fields within the current dataset.|
|DataSet| |
{{< /table >}}

### Operators

Arithmetic operators are used to combine numbers, numeric variables, numeric fields and numeric functions to get another number. Comparison operators are usually used to compare operands for a condition in a control structure such as an If statement. Boolean operators are typically used with comparison operators to generate conditions for control structures.


{{< table style="table-striped" >}}
|**Set Name**|**Formula name**|**Description**|
|:----|:----|:----|
|Arithmetic|^|Exponentiation, for example 2^3.|
| |*|Multiplication, for example 2*3.|
| |/|Division, for example 2/3.|
| |\\\\\\|Integer division, for example 2\\\\\\3.|
| |Mod|Modulus, for example 4 Mod 3.|
| |+|Addition, for example 4 + 3.|
| |-|Subtraction, for example 4 – 3.|
|Comparison|<|Less than, for example 4 < 3 false.|
| |<=|Less than or equal, for example 4 <= 3 false.|
| |>|Greater than, for example 4 > 3 true.|
| |>=|Greater than or equal, for example 4 >= 3 true.|
| |=|Equal, for example 4 = 3 false.|
| |<>|Not equal, for example 4 <> 3 true.|
| |Like|Compares a string against a pattern. For example result = string Like pattern.|
| |Is|Compares two object reference variables, for example asp Is aspose.|
|Concatenation|&|Generates a string concatenation of two expressions.|
| |+|Adds two numbers or returns the positive value of a numeric expression. Can also be used to concatenate two string expressions.|
|Logical/Bitwise|And|Performs a logical conjunction on two Boolean expressions, or a bitwise conjunction on two numeric expressions.|
| |Not|Performs logical negation on a Boolean expression, or bitwise negation on a numeric expression.|
| |Or|Performs a logical disjunction on two Boolean expressions, or a bitwise disjunction on two numeric expressions.|
| |Xor|Performs a logical exclusion on two Boolean expressions, or a bitwise exclusion on two numeric expressions.|
| |AndAlso|Performs short-circuiting logical conjunction on two expressions.|
| |OrElse|Performs short-circuiting inclusive logical disjunction on two expressions.|
|Bit Shift|>>|Performs an arithmetic left shift on a bit pattern.|
| |<<|Performs an arithmetic right shift on a bit pattern.|
{{< /table >}}

