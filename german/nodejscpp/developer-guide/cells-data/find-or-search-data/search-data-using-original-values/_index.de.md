---  
title: Daten mithilfe der Originalwerte suchen
type: docs  
weight: 380  
url: /de/nodejs-cpp/search-data-using-original-values/  
description: Lernen Sie, wie man Daten anhand der Originalwerte mit der API Aspose.Cells for Node.js via C++ durchsucht.  
keywords: Daten mit Originalwerten durchsuchen Node.js via C++, Daten mit Originalwerten finden Node.js via C++, Daten anhand der Originalwerte durchsuchen Node.js via C++, Daten anhand der Originalwerte finden Node.js via C++  
---  

{{% alert color="primary" %}}  

Manchmal wird der Wert der Daten verborgen, weil er auf irgendeine Weise formatiert ist. Zum Beispiel hat die Zelle D4 die Formel =Summe(A1:A2) und ihr Wert ist 20, aber sie ist als --- formatiert, dann ist der Wert 20 verborgen und kann nicht mit den Suchoptionen von Microsoft Excel gefunden werden. Sie können ihn jedoch mit Aspose.Cells unter Verwendung von [**LookInType.OriginalValues**](https://reference.aspose.com/cells/nodejs-cpp/lookintype) finden.  

{{% /alert %}}  

Der folgende Beispielcode verdeutlicht den obigen Punkt. Er findet die Zelle D4, die mit den Suchoptionen von Microsoft Excel nicht gefunden werden kann, aber Aspose.Cells kann sie mithilfe von [**LookInType.OriginalValues**](https://reference.aspose.com/cells/nodejs-cpp/lookintype) finden. Bitte lesen Sie die Kommentare im Code für weitere Informationen.  

## Node.js-Code zum Durchsuchen von Daten anhand der Originalwerte  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-SearchDataUsingOriginalValues.js" >}}


## Von dem Beispielcode generierte Konsolenausgabe  

Hier ist die Konsolenausgabe des obigen Beispielcodes.  

{{< highlight java >}}  

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]  

{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
