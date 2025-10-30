---
title: Arbeitsblatt des Diagramms mit Golang über C++ abrufen
linktitle: Arbeitsblatt des Diagramms abrufen
description: Erfahren Sie, wie Sie mit Aspose.Cells for C++ das zu einem Excel Diagramm gehörende Arbeitsblatt abrufen. Unser Leitfaden zeigt, wie Sie auf das Arbeitsblatt zugreifen und Operationen auf ihm ausführen, um die zugrunde liegenden Daten des Diagramms zu manipulieren.
keywords: Aspose.Cells for C++, Excel Diagramme, Arbeitsblätter, Datenmanipulation, zugrunde liegende Daten, Operationen.
type: docs
weight: 1000
url: /de/go-cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

Manchmal möchten Sie auf ein Arbeitsblatt über eine Referenz eines Diagramms zugreifen. Aspose.Cells bietet die [**Chart::GetWorksheet**](https://reference.aspose.com/cells/go-cpp/chart/getworksheet/) Methode, die die Referenz des Arbeitsblatts zurückgibt, das das Diagramm enthält.

{{% /alert %}}

Das folgende Beispiel zeigt, wie die [**Chart::GetWorksheet**](https://reference.aspose.com/cells/go-cpp/chart/getworksheet/) Methode verwendet wird. Der Code gibt zuerst den Namen des Arbeitsblatts aus, greift dann auf das erste Diagramm auf dem Arbeitsblatt zu und gibt anschließend den Namen des Arbeitsblatts erneut aus, wobei die [**Chart::GetWorksheet**](https://reference.aspose.com/cells/go-cpp/chart/getworksheet/) Methode verwendet wird.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetWorksheetOfTheChart.go" >}}
Unten ist die Konsolenausgabe, die das Beispiel des Codes ergibt. Wie Sie sehen können, druckt es den Arbeitsblattnamen beide Male gleich aus.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
