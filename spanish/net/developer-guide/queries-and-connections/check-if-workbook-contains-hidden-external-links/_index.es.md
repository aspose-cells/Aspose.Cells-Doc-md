---
title: Verificar si el libro de trabajo contiene enlaces externos ocultos
type: docs
weight: 230
url: /es/net/check-if-workbook-contains-hidden-external-links/
---

## **Escenarios de uso posibles**
A veces, el libro de trabajo contiene enlaces externos que están ocultos y no se pueden ver en Microsoft Excel. Aspose.Cells recupera todos los enlaces externos, ya sean visibles u ocultos. Sin embargo, puede verificar la propiedad [ExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible) para comprobar si el enlace externo es visible o no
## **Verificar si la Hoja de Cálculo contiene Enlaces Externos Ocultos**
El siguiente código de muestra carga el [archivo de Excel de origen](5115413.xlsx) que contiene enlaces externos ocultos. Estos enlaces no pueden verse en Microsoft Excel, pero están presentes dentro del libro de trabajo. Después de imprimir [ExternalLink.DataSource](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/datasource) y [ExternalLink.IsReferred](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isreferred), imprime la propiedad [ExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible). En la salida de la consola a continuación, se puede ver que ninguno de sus enlaces externos es visible.
### **Código de muestra**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckHiddenExternalLinks-CheckHiddenExternalLinks.cs" >}}
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
{{< app/cells/assistant language="csharp" >}}
