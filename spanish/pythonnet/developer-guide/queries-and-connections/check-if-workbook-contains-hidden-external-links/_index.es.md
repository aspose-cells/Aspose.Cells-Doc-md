---
title: Verificar si el libro de trabajo contiene enlaces externos ocultos
type: docs
weight: 230
url: /es/python-net/check-if-workbook-contains-hidden-external-links/
---

## **Escenarios de uso posibles**
A veces, el libro contiene enlaces externos ocultos que no se pueden ver en Microsoft Excel. Aspose.Cells para Python via .NET recupera todos los enlaces externos, ya sean visibles u ocultos. Sin embargo, puedes verificar la propiedad [ExternalLink.is_visible](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/is_visible) para comprobar si el enlace externo es visible o no.

## **Verificar si la Hoja de Cálculo contiene Enlaces Externos Ocultos**
El siguiente código de ejemplo carga el [archivo de Excel fuente](5115413.xlsx) que contiene enlaces externos ocultos. Estos enlaces no se pueden ver en Microsoft Excel pero están presentes en el libro de trabajo. Después de imprimir las propiedades [ExternalLink.data_source](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/data_source) y [ExternalLink.is_referred](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/is_referred), se imprime la propiedad [ExternalLink.is_visible](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/is_visible). En la salida de la consola a continuación, puedes ver que todos sus enlaces externos no son visibles.

### **Código de muestra**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-CheckHiddenExternalLinks.py" >}}

### **Salida de la consola**
Aquí está la salida de la consola del código de muestra anterior cuando se ejecuta con el [archivo de Excel de muestra proporcionado](5115413.xlsx).



{{< highlight java >}}

 Data Source: C:\International\DDB\FAS 133\Swap Rates\GS_1M_3M_1_2_5_¥$_(B)IRSwaps_0400.xls

Is Referred: True

Is Visible: False

Data Source: C:\DIST DAY\MAY TEMPLATES\030601t.xls

Is Referred: True

Is Visible: False

Data Source: C:\AREVIEW\2002 Controllable\Autobrct.xls

Is Referred: True

Is Visible: False

Data Source: C:\CARDSFO\Main Files\Rate Forecast\FY 11\IFR 11 01 (New Model REPORTS 11.08.07).xls

Is Referred: True

Is Visible: False

{{< /highlight >}}

