---
title: Configurar el modo de cálculo de fórmulas del libro con Golang mediante C++
linktitle: Configuración del modo de cálculo de fórmulas del libro de trabajo
description: Este artículo presenta cómo configurar el modo de cálculo de fórmulas de un libro en Microsoft Excel con la biblioteca Aspose.Cells usando C++. Al cargar un archivo de Excel existente o crear uno nuevo, podemos usar el método proporcionado por Aspose.Cells para establecer el modo de cálculo de fórmulas y obtener el resultado. Finalmente, guardamos el archivo de Excel modificado en disco.
keywords: Aspose.Cells, Excel, libro de trabajo, modo de cálculo de fórmulas, configuración, C++
type: docs
weight: 110
url: /es/go-cpp/setting-formula-calculation-mode-of-workbook/
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

Aspose.Cells también te permite configurar el **Modo de cálculo de fórmulas** usando la propiedad de modo [**FormulaSettings.GetCalculationMode()**](https://reference.aspose.com/cells/go-cpp/formulasettings/getcalculationmode/). Puedes asignarle la enumeración [**CalcModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/calcmodetype/) que tiene uno de los siguientes valores:

- CalcModeType::Automatic
- CalcModeType::AutomaticExceptTable
- CalcModeType::Manual

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingFormulaCalculationModeOfWorkbook.go" >}}
