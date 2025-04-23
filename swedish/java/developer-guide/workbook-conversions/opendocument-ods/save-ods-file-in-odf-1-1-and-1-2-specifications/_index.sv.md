---
title: Spara ODS fil i ODF 1.1, 1.2 och 1.3 specifikationer
type: docs
weight: 170
url: /sv/java/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells stöder att spara (**OpenDocument Spreadsheet**) ODS-fil i (**OpenDocument Format**) ODF 1.1, 1.2 och ODF 1.3 specifikationer. Aspose.Cells har lagt till [**OdsSaveOptions.setOdfStrictVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/odssaveoptions/#setOdfStrictVersion-int-) egenskap för att använda ODF-versionen för att spara ODS-filer. Standardvärdet för denna egenskap är [**OpenDocumentFormatVersionType.ODF_12**](https://reference.aspose.com/cells/java/com.aspose.cells/opendocumentformatversiontype/#ODF-12), så ODS-fil som sparas utan dessa särskilda inställningar kommer att använda 1.2-specifikationen.

{{% /alert %}}

Det följande kodexemplet skapar arbetsbokobjektet, lägger till värden i cell A1 i den första kalkylbladet och sparar sedan ODS-filen enligt ODF 1.1 och 1.2-specifikationer. Som standard sparas ODS-filen enligt ODF 1.2-specifikationen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveODSfile-SaveODSfile.java" >}}
{{< app/cells/assistant language="java" >}}
