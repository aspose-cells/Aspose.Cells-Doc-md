---
title: CSS beim Speichern in HTML deaktivieren
type: docs
weight: 320
url: /de/java/disable-css-while-saving-to-html/
---

## **Mögliche Verwendungsszenarien**

Wenn Sie Ihre Excel-Datei in ein einseitiges HTML speichern, werden die CSS-Elemente normalerweise im HTML-Dokument im HEAD-Bereich eingebettet. Wenn Sie diese Datei als Inhalt/Body einer E-Mail anhängen, werden die CSS-Elemente von den meisten E-Mail-Clients entfernt, was zu unsachgemäßer Darstellung führt. Die Version 24.12 von Aspose.Cells führt eine Option ein, mit der CSS optional deaktiviert werden kann, sodass Stile direkt innerhalb der HTML-Elemente angewendet werden. Wenn Sie das HTML als Inhalt/Body der E-Mail setzen möchten, verwenden Sie bitte die [**HtmlSaveOptions.DisableCss**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions/properties/#DisableCss) Eigenschaft und setzen Sie sie auf **true**.



## **CSS beim Speichern in HTML deaktivieren**

Der folgende Beispielcode zeigt die Verwendung der [**HtmlSaveOptions.DisableCss**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions/properties/#DisableCss) Eigenschaft. 



## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-java-HTML-DisableCss-1.java" >}}
{{< app/cells/assistant language="java" >}}
