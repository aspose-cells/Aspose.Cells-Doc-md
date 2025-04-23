---
title: Crear, Manipular o Eliminar Escenarios de Hojas de Cálculo
linktitle: Gestionar Escenarios
type: docs
weight: 120
url: /es/java/create-manipulate-or-remove-scenarios-from-worksheets/
---

{{% alert color="primary" %}}

A veces, necesitas crear, manipular o eliminar escenarios en hojas de cálculo. Un escenario es un modelo de suposición que incluye celdas de entrada variables vinculadas por una o más fórmulas. Antes de crear un escenario, diseña una hoja de cálculo de manera que contenga al menos una fórmula que dependa de celdas en las cuales se puedan insertar diferentes valores. El siguiente ejemplo muestra cómo crear y eliminar escenarios de una hoja de cálculo utilizando las APIs de Aspose.Cells.

{{% /alert %}}

Aspose.Cells proporciona algunas clases útiles, por ejemplo [**ScenarioCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioCollection), [**Scenario**](https://reference.aspose.com/cells/java/com.aspose.cells/Scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCellCollection) y [**ScenarioInputCell**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCell). También proporciona la propiedad [**Worksheet.Scenarios**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Scenarios). El código de muestra a continuación abre un archivo de Excel XLSX (que contiene algunos escenarios) y elimina un escenario existente de la hoja de cálculo. También agrega un nuevo escenario antes de guardar el archivo de Excel. Utiliza un archivo de plantilla muy sencillo que contiene un escenario.

Después de ejecutar el código, se elimina un escenario existente y se agrega un nuevo escenario a la hoja de cálculo.

**El archivo de salida**

![todo:image_alt_text](create-manipulate-or-remove-scenarios-from-worksheets_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateScenariosfromWorksheets-CreateScenariosfromWorksheets.java" >}}
{{< app/cells/assistant language="java" >}}
