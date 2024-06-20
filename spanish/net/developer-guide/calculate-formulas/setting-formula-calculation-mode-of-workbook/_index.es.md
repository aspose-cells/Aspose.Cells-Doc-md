---
title: Configuración del modo de cálculo de fórmulas del libro de trabajo
description: Este artículo presenta cómo establecer el modo de cálculo de fórmulas de un libro de trabajo en Microsoft Excel con la biblioteca Aspose.Cells. Al cargar un archivo de Excel existente o crear un nuevo archivo de Excel, podemos usar el método proporcionado por Aspose.Cells para establecer el modo de cálculo de fórmulas y obtener el resultado. Finalmente, guardamos el archivo de Excel modificado en el disco.
keywords: Aspose.Cells, Excel, libro de trabajo, modo de cálculo de fórmulas, configuraciones
type: docs
weight: 110
url: /es/net/setting-formula-calculation-mode-of-workbook/
---

{{% alert color="primary" %}}

Microsoft Excel te permite establecer el modo de cálculo de fórmulas, es decir, la forma en que se calculan las fórmulas. Hay tres valores posibles:

- Automático: recalcula cada vez que algo cambia, y cada vez que se abre un libro.
- Automático excepto para tablas de datos: recalcula cada vez que algo cambia, pero deja fuera las tablas de datos.
- Manual: recalcula solo cuando el usuario lo solicita explícitamente presionando F9 o CTRL+ALT+F9, o cuando se guarda el libro.

{{% /alert %}}

Para establecer el modo de cálculo de fórmulas en Microsoft Excel:

1. Selecciona **Fórmulas** y luego **Opciones de cálculo**.
1. Selecciona una de las opciones.

Aspose.Cells también te permite configurar el **Modo de cálculo de fórmulas** usando la propiedad de modo [**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/calculationmode). Puedes asignarle la enumeración [**CalcModeType**](https://reference.aspose.com/cells/net/aspose.cells/calcmodetype) que tiene uno de los siguientes valores:

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingFormulaCalculationModeWorkbook-1.cs" >}}
