---
title: Crear, manipular o eliminar escenarios de las hojas de trabajo
linktitle: Administrar escenarios
type: docs
weight: 190
url: /es/net/create-manipulate-or-remove-scenarios-from-worksheets/
---
{{% alert color="primary" %}}

veces, necesita crear, manipular o eliminar escenarios en hojas de cálculo. Un escenario es un '¿y si?' modelo que incluye celdas de entrada de variables vinculadas por una o más fórmulas. Antes de crear un escenario, diseñe la hoja de trabajo para que contenga al menos una fórmula que dependa de las celdas en las que se pueden insertar diferentes valores. El siguiente ejemplo muestra cómo crear y eliminar escenarios de una hoja de trabajo en un libro de trabajo a través de las API Aspose.Cells.

{{% /alert %}}

Aspose.Cells proporciona algunas clases útiles, por ejemplo,[**ScenarioCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenariocollection), [**Guión**](https://reference.aspose.com/cells/net/aspose.cells/scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcellcollection) , y[**Celda de entrada de escenario**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcell) clases También proporciona la[**Hoja de trabajo.Escenarios**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/scenarios)propiedad. El código de ejemplo siguiente abre un archivo de Excel XLSX que contiene algunos escenarios y elimina un escenario existente. También agrega un nuevo escenario a la hoja de trabajo antes de guardar el archivo de Excel. El ejemplo utiliza un archivo de plantilla muy simple que contiene un escenario.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateManipulateRemoveScenarios-1.cs" >}}
