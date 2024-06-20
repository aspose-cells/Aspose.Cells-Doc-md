---
title: Crear, Manipular o Eliminar Escenarios de Hojas de Cálculo
linktitle: Gestionar Escenarios
type: docs
weight: 190
url: /es/net/create-manipulate-or-remove-scenarios-from-worksheets/
description: En este artículo, aprenderás cómo crear, manipular o eliminar Escenarios de Hojas de cálculo de Excel programáticamente usando la biblioteca de C# con la API .NET.
keywords: crear escenario hoja de cálculo c#, eliminar escenario hoja de cálculo excel c#, manipular escenario hoja de cálculo c#
---

{{% alert color="primary" %}}

A veces, necesitas crear, manipular o eliminar escenarios en hojas de cálculo. Un escenario es un modelo de 'qué pasaría si' que incluye celdas de entrada variables vinculadas por una o más fórmulas. Antes de crear un escenario, diseña la hoja de cálculo para que contenga al menos una fórmula que dependa de celdas en las que se puedan insertar diferentes valores. El siguiente ejemplo muestra cómo crear y eliminar escenarios de una hoja de cálculo en un libro mediante las API de Aspose.Cells.

{{% /alert %}}

Aspose.Cells proporciona algunas clases útiles, por ejemplo, las clases [**ScenarioCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenariocollection), [**Scenario**](https://reference.aspose.com/cells/net/aspose.cells/scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcellcollection), y [**ScenarioInputCell**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcell). También proporciona la propiedad [**Worksheet.Scenarios**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/scenarios). El código de ejemplo a continuación abre un archivo de Excel XLSX que contiene algunos escenarios y elimina un escenario existente. También agrega un nuevo escenario a la hoja de cálculo antes de guardar el archivo de Excel. El ejemplo utiliza un archivo de plantilla muy simple que contiene un escenario.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateManipulateRemoveScenarios-1.cs" >}}
