---
title: Compruebe si el libro de trabajo contiene enlaces externos ocultos
type: docs
weight: 230
url: /es/net/check-if-workbook-contains-hidden-external-links/
---
## **Posibles escenarios de uso**
 veces, el libro de trabajo contiene enlaces externos que están ocultos y no se pueden ver en Microsoft Excel. Aspose.Cells recupera todos los enlaces externos, ya sean visibles u ocultos. Sin embargo, puede consultar la[ExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible)propiedad para verificar si el enlace externo es visible o no
## **Compruebe si el libro de trabajo contiene enlaces externos ocultos**
 El siguiente código de ejemplo carga el[archivo fuente excel](5115413.xlsx) que contiene enlaces externos ocultos. Estos enlaces no se pueden ver en Microsoft Excel pero están presentes dentro del libro de trabajo. Después de imprimir[ExternalLink.DataSource](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/datasource) y[ExternalLink.IsReferred](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isreferred) propiedad, imprime la[ExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible)propiedad. En la salida de la consola a continuación, verá que todos sus enlaces externos no son visibles.
### **Código de muestra**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckHiddenExternalLinks-CheckHiddenExternalLinks.cs" >}}
### **Salida de consola**
 Aquí está la salida de la consola del código de muestra anterior cuando se ejecuta con el dado[ejemplo de archivo de Excel](5115413.xlsx).



{{< highlight "java" >}}

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
