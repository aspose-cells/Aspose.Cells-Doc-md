---
title : "Using ICustomFunction Feature" 
description : "" 
weight : 12038 
toc : false
type: docs
url: /cpp/developerguide/formulas/using+icustomfunction+feature/
---

# Aspose.Cells for C++ : Using ICustomFunction Feature


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Introduction](#introduction)
*   2 [Using ICustomFunction Feature](#using-icustomfunction-feature)
*   3 [Sample Code](#sample-code)
*   4 [Console Output](#console-output)
{{< /panel >}}
 

## Introduction

This article provides an understanding of how to use the `ICustomFunction` feature to implement custom functions with Aspose.Cells APIs.

The `ICustomFunction` interface allows you to add custom formula calculation functions to extend the Aspose.Cells core calculation engine in order to meet certain requirements. This feature is useful to define custom (user defined) functions in a template file or in a code where the custom function can be implemented and evaluated using Aspose.Cells APIs like any other default Microsoft Excel function.

## Using ICustomFunction Feature

The following sample code implements the `ICustomFunction` interface which evaluates and returns the values of the two custom functions i.e. `MySampleFunc()` and `YourSampleFunc()`. These custom functions are inside the cells A1 and A2 respectively. Then it calls the `IWorkbook.CalculateFormula(false, ICustomFunction)` method to invoke the implementation of `ICustomFunction.CalculateCustomFunction()` method. Then, `it prints the values of A1 and A2` on console which are actually the values returned by `ICustomFunction.CalculateCustomFunction()`. Please see the `Console Output` of the sample code below for more help.

## Sample Code

## Console Output

{{< code lang="cs" >}}
Value of A1: MY sample function was called successfully.
Value of A2: YOUR sample function was called successfully.
{{< /code >}}

