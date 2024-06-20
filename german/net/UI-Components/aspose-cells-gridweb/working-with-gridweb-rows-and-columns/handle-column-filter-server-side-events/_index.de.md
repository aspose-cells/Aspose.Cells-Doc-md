---
title: Behandeln von Serverseitigen Spaltenfilterereignissen
type: docs
weight: 90
url: /de/net/aspose-cells-gridweb/handle-column-filter-server-side-events/
keywords: GridWeb,filter,OnBeforeColumnFilter,OnAfterColumnFilter
description: Dieser Artikel zeigt, wie man das Spaltenfilterereignis in GridWeb behandelt.
---

{{% alert color="primary" %}} 

Die Datenfilterung ist wahrscheinlich die am häufigsten verwendete Excel-Funktion, die es Ihnen ermöglicht, die Daten basierend auf bestimmten Kriterien zu filtern. Gefilterte Daten zeigen nur die Zeilen an, die die Bedingung erfüllen, indem sie die Zeilen ausblenden, die die Kriterien nicht erfüllen.
Das Aspose.Cells.GridWeb-Komponente bietet die Möglichkeit, die Datenfilterung über seine Benutzeroberfläche durchzuführen. Um die Fähigkeiten zu erweitern, bietet die Aspose.Cells.GridWeb-Komponente auch zwei Ereignisse, die als Rückruf für den Filtermechanismus dienen können, der über die GridWeb-Benutzeroberfläche durchgeführt wird.

{{% /alert %}} 
## **Behandlung von Serverseitigen Ereignissen bei Anwendung des Spaltenfilters**
Es gibt zwei Hauptereignisse, wie nachstehend beschrieben.

1. OnBeforeColumnFilter: Wird vor der Anwendung des Filters auf eine Spalte ausgelöst.
1. OnAfterColumnFilter: Wird ausgelöst, nachdem der Filter auf eine Spalte angewendet wurde.

Hier ist das ASPX-Skript der Aspose.Cells.GridWeb-Komponente, um die oben genannten Ereignisse hinzuzufügen und zuzuweisen.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents-HandleColumnFilterEvents.aspx" >}}



Diese Ereignisse können verwendet werden, um nützliche Informationen zum Filterprozess zu erhalten, wie beispielsweise den Spaltenindex und den Wert, auf den der Filter angewendet werden soll. Im Folgenden finden Sie ein Codebeispiel, das die Verwendung des OnBeforeColumnFilter-Ereignisses zum Abrufen des Spaltenindex und des Werts, den der Benutzer in der GridWeb-Benutzeroberfläche für das Filtern ausgewählt hat, demonstriert.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-BeforeColumnFilter.cs" >}}


Andererseits, wenn die Anforderung darin besteht, die Anzahl der gefilterten Zeilen nach Anwendung des Filters zu erhalten, können Sie das OnAfterColumnFilter-Ereignis wie unten gezeigt verwenden.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-AfterColumnFilter.cs" >}}

{{% alert color="primary" %}} 

Sehen Sie sich die Einführung zu allen [Arbeiten mit GridWeb-Ereignissen](/cells/de/net/aspose-cells-gridweb/working-with-gridweb-events/) sowie einige Details dazu, wie man diese Ereignisse behandelt, an.

{{% /alert %}}
