---
title: Konvertera revision av XLSB till XLSM
type: docs
weight: 2200
url: /sv/java/convert-revision-of-xlsb-to-xlsm/
---

{{% alert color="primary" %}} 

Aspose.Cells stöder nu att helt konvertera revisioner av XLSB-filer till XLSM-filer. Revisionerna finns i sökvägen \xl\revisions. Du kan se dem genom att ändra filändelsen på XLSB-filen till ZIP. Sökvägen \xl\revisions innehåller filer som slutar med .bin-förlängningar.

När du konverterar din XLSB-fil till XLSM-fil med Aspose.Cells, konverteras dessa .bin-filer framgångsrikt till .xml-filer, som visas i dessa två skärmbilder.

{{% /alert %}} 
## **Konvertera revidering av XLSB till XLSM**
Följande skärmbild visar .bin-filerna i sökvägen \xl\revisions för XLSB-filen.

![todo:image_alt_text](convert-revision-of-xlsb-to-xlsm_1.png)

Följande skärmbild visar hur .bin-filerna har konverterats till .xml-filer när XLSB-filen konverteras till XLSM-format med Aspose.Cells.

![todo:image_alt_text](convert-revision-of-xlsb-to-xlsm_2.png)

Här är koden för att konvertera XLSB-filen till XLSM-format med hjälp av Aspose.Cells.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConvertRevisionOfXLSBtoXLSM-ConvertRevisionOfXLSBtoXLSM.java" >}}
{{< app/cells/assistant language="java" >}}
