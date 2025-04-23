---
title: Kunskapsbas för kalkylbladsredigerare
type: docs
weight: 30
url: /sv/java/spreadsheet-editor-knowledge-base/
---

## **Bädda in HTML5 Spreadsheet Editor var som helst**

HTML5 Spreadsheet Editor kan bäddas in på vilken webbplats, blogg och forum som helst för att dela kalkylblad över internet. Den kan bäddas in som en fristående redigerare eller så kan den laddas med en kalkylbladsfil.

**Bädda in som fristående redigerare**

För att bädda in som en fristående redigerare, använd HTML IFRAME-taggen för att lägga till på webbplatsen. Till exempel:

{{< highlight html >}}

 <iframe src="http://spreadsheet-editor.aspose.com/" width="800" height="600">

    Your web browser does not support IFRAMEs

</iframe>

{{< /highlight >}}

**Bädda in med ett kalkylblad**

För att ladda en kalkylblad i en inbäddad redigerare **url** parameter. Till exempel:

{{< highlight html >}}

 <iframe src="http://spreadsheet-editor.aspose.com/?url=http://example.com/Sample.xlsx" width="800" height="600">

    Your web browser does not support IFRAMEs

</iframe>

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
