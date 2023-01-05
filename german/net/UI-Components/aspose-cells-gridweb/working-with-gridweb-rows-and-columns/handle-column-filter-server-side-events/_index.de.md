---
title: Behandeln von Server-Side-Events für Spaltenfilter
type: docs
weight: 90
url: /de/net/handle-column-filter-server-side-events/
---
{{% alert color="primary" %}} 

Die Datenfilterung ist wahrscheinlich die am weitesten verbreitete Excel-Funktion, mit der Sie die Daten nach bestimmten Kriterien filtern können. Gefilterte Daten zeigen nur die Zeilen an, die die Bedingung erfüllen, indem die Zeilen ausgeblendet werden, die die Kriterien nicht erfüllen.
Aspose.Cells. Die GridWeb-Komponente bietet die Möglichkeit, die Datenfilterung über ihre Schnittstelle durchzuführen. Um ihre Fähigkeiten zu erweitern, stellt die Aspose.Cells.GridWeb-Komponente auch zwei Ereignisse bereit, die als Rückruf für den Filtermechanismus dienen können, der über die GridWeb-UI erfolgt.

{{% /alert %}} 
## **Behandeln von serverseitigen Ereignissen beim Anwenden des Spaltenfilters**
Es gibt zwei Hauptereignisse, wie unten beschrieben.

1. OnBeforeColumnFilter: Wird ausgelöst, bevor der Filter auf eine Spalte angewendet wird.
1. OnAfterColumnFilter: Wird ausgelöst, nachdem der Filter auf eine Spalte angewendet wurde.

Hier ist das ASPX-Skript der Komponente Aspose.Cells.GridWeb zum Hinzufügen und Zuweisen der oben genannten Ereignisse.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents-HandleColumnFilterEvents.aspx" >}}



Diese Ereignisse können verwendet werden, um nützliche Informationen über den Filterprozess zu erhalten, z. B. Spaltenindex und Wert, auf den der Filter angewendet werden muss. Das folgende Snippet zeigt die Verwendung des OnBeforeColumnFilter-Ereignisses zum Abrufen des Spaltenindex und -werts, den der Benutzer auf der GridWeb-Benutzeroberfläche zum Filtern ausgewählt hat.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-BeforeColumnFilter.cs" >}}


Wenn andererseits die Anforderung darin besteht, die Anzahl der gefilterten Zeilen zu erhalten, nachdem der Filter angewendet wurde, können Sie das OnAfterColumnFilter-Ereignis wie unten gezeigt verwenden.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-AfterColumnFilter.cs" >}}

{{% alert color="primary" %}} 

 Überprüfen Sie die Einführung für alle[Arbeiten mit GridWeb-Ereignissen](/cells/de/net/working-with-gridweb-events/) zusammen mit einigen Details zum Umgang mit diesen Ereignissen.

{{% /alert %}}
