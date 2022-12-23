---
title: Crear, manipular o eliminar escenarios de las hojas de trabajo
linktitle: Administrar escenarios
type: docs
weight: 120
url: /es/java/create-manipulate-or-remove-scenarios-from-worksheets/
---
{{% alert color="primary" %}}

A veces, necesita crear, manipular o eliminar escenarios en hojas de cálculo. Un escenario es un modelo hipotético con nombre que incluye celdas de entrada de variables unidas por una o más fórmulas. Antes de crear un escenario, diseñe una hoja de trabajo para que contenga al menos una fórmula que dependa de las celdas en las que se pueden insertar diferentes valores. El siguiente ejemplo muestra cómo crear y eliminar escenarios de una hoja de trabajo utilizando las API Aspose.Cells.

{{% /alert %}}

 Aspose.Cells proporciona algunas clases útiles, por ejemplo[**ScenarioCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioCollection), [**Guión**](https://reference.aspose.com/cells/java/com.aspose.cells/Scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCellCollection) y[**Celda de entrada de escenario**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCell) . También proporciona la[**Hoja de trabajo.Escenarios**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Scenarios)propiedad. El código de ejemplo siguiente abre un archivo de Excel XLSX (que contiene algunos escenarios) y elimina un escenario existente de la hoja de trabajo. También agrega un nuevo escenario antes de guardar el archivo de Excel. Utiliza un archivo de plantilla muy simple que contiene un escenario.

Después de ejecutar el código, se elimina un escenario existente y se agrega un nuevo escenario a la hoja de trabajo.

**El archivo de salida**

![todo:imagen_alternativa_texto](create-manipulate-or-remove-scenarios-from-worksheets_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateScenariosfromWorksheets-CreateScenariosfromWorksheets.java" >}}
