---  
title: Größe der Datenbeschriftungsform des Diagramms an den Text anpassen mit Golang über C++  
description: Erfahren Sie, wie Sie die Form der Datenbeschriftung in einem Diagramm anpassen, um den Text in Aspose.Cells for C++ einzupassen. Unser Leitfaden zeigt Ihnen, wie Sie die Größe und Form des Beschriftungskontainers anpassen, um sicherzustellen, dass der Text korrekt angezeigt wird, ohne abgeschnitten oder überlappt zu werden.  
keywords: Aspose.Cells for C++, Diagrammerstellung, Datenbeschriftungen, Formenänderung, Textanpassung, Abschneidung, Überlappung.  
type: docs  
weight: 220  
url: /de/go-cpp/resize-chart-s-data-label-shape-to-fit-text/  
---  

{{% alert color="primary" %}}  

Die Excel-Anwendung bietet die Option **Form an Text anpassen** für Diagrammdatenbeschriftungen, um die Größe der Form zu erhöhen, damit der Text hineinpasst.  

{{% /alert %}}  

## **So passen Sie die Form der Datenbeschriftung in einem Diagramm an, damit der Text in Microsoft Excel passt**  

Diese Option kann in der Excel-Benutzeroberfläche durch Auswahl einer beliebigen Datenbeschriftung im Diagramm aufgerufen werden. Klicken Sie mit der rechten Maustaste und wählen Sie das Menü **Datenbeschriftungen formatieren**. Unter dem Tab **Größe & Eigenschaften** expandieren Sie **Ausrichtung**, um die zugehörigen Eigenschaften einschließlich der Option **Form ändern, um Text anzupassen** anzuzeigen.  

## **So passen Sie die Form der Diagrammdatenbeschriftungen mit Aspose.Cells for C++ an**  

Um die Excel-Funktion nachzuahmen, die die Formen der Datenbeschriftungen an den Text anpasst, haben die Aspose.Cells APIs die boolesche Eigenschaft [**DataLabels.IsResizeShapeToFitText**](https://reference.aspose.com/cells/go-cpp/charttextframe/isresizeshapetofittext/) freigegeben. Der folgende Code zeigt ein einfaches Nutzungsszenario der [**DataLabels.IsResizeShapeToFitText**](https://reference.aspose.com/cells/go-cpp/charttextframe/isresizeshapetofittext/)-Eigenschaft.  

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ResizeChartSDataLabelShapeToFitText.go" >}}  
