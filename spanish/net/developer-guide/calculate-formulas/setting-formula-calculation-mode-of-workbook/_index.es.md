---
title: Configuración del modo de cálculo de fórmulas del libro de trabajo
description: Este artículo presenta cómo configurar el modo de cálculo de fórmulas de un libro en Excel Microsoft con la biblioteca Aspose.Cells. Al cargar un archivo de Excel existente o crear un nuevo archivo de Excel, podemos usar el método proporcionado por Aspose.Cells para configurar el modo de cálculo de la fórmula y obtener el resultado. Finalmente, guardamos el archivo Excel modificado en el disco.
keywords: Aspose.Cells, Excel, workbook, formula calculation mode, settings
type: docs
weight: 110
url: /es/net/setting-formula-calculation-mode-of-workbook/
---
{{% alert color="primary" %}}

Microsoft Excel le permite configurar el modo de cálculo de fórmulas, es decir, la forma en que se calculan las fórmulas. Hay tres valores posibles:

- Automático: vuelve a calcular cada vez que se cambia algo y cada vez que se abre un libro.
- Automático excepto para las tablas de datos: recalcula cada vez que se cambia algo, pero omitiendo las tablas de datos.
- Manual: vuelva a calcular solo cuando el usuario lo solicite explícitamente presionando F9 o CTRL+ALT+F9, o cuando se guarde el libro.

{{% /alert %}}

Para configurar el modo de cálculo de fórmulas en Microsoft Excel:

1.  Seleccionar**Fórmulas** y luego *Opciones de cálculo**.
1. Seleccione una de las opciones.

 Aspose.Cells también le permite configurar el**Modo de cálculo de fórmulas** usando[**Configuración de fórmula.Modo de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/calculationmode) propiedad del modo. Puedes asignarle el[**Tipo de modo de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/calcmodetype)enumeración que tiene uno de los siguientes valores:

- CalcModeType.Automático
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingFormulaCalculationModeWorkbook-1.cs" >}}
