---
title: Wissensdatenbank des Tabellen Editors
type: docs
weight: 30
url: /de/java/spreadsheet-editor-knowledge-base/
---

## **Einbetten des HTML5 Tabellen-Editors überall**

Der HTML5 Tabellen-Editor kann in jede Webseite, Blog und Foren eingebettet werden, um Tabellen über das Internet zu teilen. Er kann als eigenständiger Editor eingebettet werden oder Sie können ihn mit einer Tabellendatei laden.

**Als eigenständigen Editor einbetten**

Um als eigenständiger Editor eingebettet zu werden, verwenden Sie das HTML IFRAME-Tag, das in die Webseite eingefügt wird. Zum Beispiel:

{{< highlight html >}}

 <iframe src="http://spreadsheet-editor.aspose.com/" width="800" height="600">

    Your web browser does not support IFRAMEs

</iframe>

{{< /highlight >}}

**Mit einer Tabelle einbetten**

Um eine Tabelle in einen eingebetteten Editor zu laden, verwenden Sie den **url**-Parameter. Zum Beispiel:

{{< highlight html >}}

 <iframe src="http://spreadsheet-editor.aspose.com/?url=http://example.com/Sample.xlsx" width="800" height="600">

    Your web browser does not support IFRAMEs

</iframe>

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
