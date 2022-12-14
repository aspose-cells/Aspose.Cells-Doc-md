---
title: Configuración del modo de cálculo de fórmulas del libro de trabajo
type: docs
weight: 110
url: /es/net/setting-formula-calculation-mode-of-workbook/
---
{{% alert color="primary" %}}

Microsoft Excel le permite configurar el modo de cálculo de fórmulas, es decir, la forma en que se calculan las fórmulas. Hay tres valores posibles:

- Automático: vuelve a calcular cada vez que se cambia algo y cada vez que se abre un libro.
- Automático excepto para las tablas de datos: vuelve a calcular cada vez que se cambia algo, pero omite las tablas de datos.
- Manual: vuelva a calcular solo cuando el usuario lo solicite explícitamente presionando F9 o CTRL+ALT+F9, o cuando se guarde el libro.

{{% /alert %}}

Para configurar el modo de cálculo de fórmula en Microsoft Excel:

1.  Seleccione**Fórmulas** y entonces**Opciones de cálculo**.
1. Seleccione una de las opciones.

 Aspose.Cells también le permite configurar el**Modo de cálculo de fórmula** usando[**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/calculationmode) propiedad de modo. Puedes asignarle el[**CalcModeType**](https://reference.aspose.com/cells/net/aspose.cells/calcmodetype)enumeración que tiene uno de los siguientes valores:

- CalcModeType.Automático
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingFormulaCalculationModeWorkbook-1.cs" >}}
