---  
title: Zeilenumbrüche und Textumbruch
linktitle: Zeilenumbrüche und Textumbruch  
description: Wie man Textumbruch und Zeilenumbruch mit der Aspose.Cells Bibliothek in Node.js via C++ implementiert. Mit der Aspose.Cells Bibliothek können Sie Text in Zellen einfach einfügen und die Textumbruchmethode festlegen, wie manueller Zeilenumbruch, Wortumbruch usw. Dieses Dokument beschreibt, wie diese Funktionen implementiert werden und enthält Beispielcode.  
keywords: Aspose.Cells, Zeilenumbrüche, Textumbrüche, Textlayout Node.js via C++  
type: docs  
weight: 60  
url: /de/nodejs-cpp/line-breaks-and-text-wrapping/  
---  

{{% alert color="primary" %}}  
Um sicherzustellen, dass der Text in einer Zelle gelesen werden kann, können explizite Zeilenumbrüche und Textumbrüche angewendet werden. Textumbrüche verwandeln eine Zeile in mehrere in einer Zelle, wobei explizite Zeilenumbrüche genau dort eingefügt werden, wo Sie sie haben möchten.  
{{% /alert %}}  

## **Text in einer Zelle umbrechen**  
 Um Text in einer Zelle umzubrechen, verwenden Sie die [**Aspose.Cells.Style.setIsTextWrapped(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIsTextWrapped-boolean-) Methode.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-WrapTextInCell.js" >}}


## **Explizite Zeilenumbrüche verwenden**  
 Sie können '\n' in JavaScript verwenden, um in einer Zelle explizite Zeilenumbrüche einzufügen.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-UseExplicitLineBreaks.js" >}}



{{< app/cells/assistant language="nodejs-cpp" >}}
