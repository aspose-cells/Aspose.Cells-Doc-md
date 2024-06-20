---
title: Spara ODS fil i ODF 1.1 och 1.2 specifikationer
type: docs
weight: 170
url: /sv/java/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells stöder att spara (**OpenDocument Spreadsheet**) ODS-fil enligt (**OpenDocument Format**) ODF 1.1 och ODF 1.2-specifikationer. Aspose.Cells har lagt till egenskapen [**OdsSaveOptions.setStrictSchema11()**](https://reference.aspose.com/cells/java/com.aspose.cells/odssaveoptions#IsStrictSchema11) för att använda ODF 1.1-specifikationen för att spara ODS-filer. Standardvärdet för denna egenskap är **false**, så ODS-filen som sparas utan dessa specialinställningar kommer att använda 1.2-specifikationen.

{{% /alert %}}

Det följande kodexemplet skapar arbetsbokobjektet, lägger till värden i cell A1 i den första kalkylbladet och sparar sedan ODS-filen enligt ODF 1.1 och 1.2-specifikationer. Som standard sparas ODS-filen enligt ODF 1.2-specifikationen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveODSfile-SaveODSfile.java" >}}
