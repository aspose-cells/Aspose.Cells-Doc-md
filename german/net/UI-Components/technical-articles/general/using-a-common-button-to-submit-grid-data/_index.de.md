---
title: Verwendung einer allgemeinen Schaltfläche zum Übermitteln von Gitterdaten
type: docs
weight: 20
url: /de/net/aspose-cells-gridweb/using-a-common-button-to-submit-grid-data/
keywords: GridWeb, übermitteln, Schaltfläche, benutzerdefiniert
description: Dieser Artikel beschreibt die Verwendung der Übermittlungsschaltfläche in GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb bietet einige integrierte Befehlsschaltflächen wie **Übermitteln** und **Speichern**. Verwenden Sie diese Schaltflächen, um entsprechende Aufgaben auszuführen.

Dieser Artikel zeigt, wie Daten an einen Server übermittelt werden, nicht nur durch Klicken auf die integrierte **Speichern**-Befehlsschaltfläche von GridWeb, sondern durch Klicken auf eine gemeinsame ASP.NET-Schaltfläche (Websteuerelement). Der Zweck dieses Artikels besteht darin, die Flexibilität von Aspose.Cells.GridWeb zu zeigen. Darüber hinaus verwendet dieser Artikel auch spezielle Funktionen, die von Aspose.Cells.GridWeb bereitgestellt werden, die im Client-Seitenskript verwendet werden können.

{{% /alert %}} 
## **Übermittlung von Gitterdaten unter Verwendung einer ASP.NET-Schaltfläche**
Aspose.Cells.GridWeb bietet drei integrierte Schaltflächen (**Übermitteln**, **Speichern** und **Rückgängig**). Nach der Bearbeitung in GridWeb kann ein Benutzer auf die **Übermitteln**- oder **Speichern**-Schaltfläche in der Registerkarte klicken, um GridWeb Daten an den Server zu übermitteln. Wenn der Benutzer auf eine Blattregisterkarte klickt, führt die GridWeb-Steuerung dieselbe Aufgabe wie die der integrierten Befehlsschaltflächen aus. Aspose.Cells.GridWeb unterstützt auch das Hinzufügen dieser Funktionalität zu einer allgemeinen ASP.NET-Schaltfläche, jedoch muss einige zusätzliche Code zur Anwendung hinzugefügt werden.
### **1. Erstellen einer Testanwendung**
Öffnen Sie Ihre Visual Studio.NET-IDE und erstellen Sie ein neues ASP.NET-Webanwendungsprojekt. Nachdem die Anwendung erstellt wurde, wird eine Standard-WebForm1.aspx-Seite zu Ihrem Projekt hinzugefügt. Ziehen Sie das GridWeb-Steuerelement aus Ihrem Toolbox auf die Webform. Wenn Sie das GridWeb-Steuerelement nicht in Ihrer Toolbox finden können, verweisen Sie auf diese Seite: [Integrieren von Aspose.Cells Grid-Steuerungen mit Visual Studio.NET](/cells/de/net/integrieren-von-aspose-cells-grid-steuerungen-mit-visual-studio-net/) um mehr darüber zu erfahren. Nachdem das GridWeb-Steuerelement Ihrer Webform hinzugefügt wurde, fügen Sie auch ein Schaltflächen-Websteuerelement aus der Toolbox zu Ihrer Webform hinzu.
### **2. Hinzufügen von Code zum Page_Load-Ereignis**
Jetzt ist es an der Zeit, dem Page_Load-Ereignis der Webform etwas Code hinzuzufügen. Sie können in der Designansicht auf die Webform doppelklicken und die VS.NET-IDE bringt Sie automatisch zum Page_Load-Ereignishandler, wo Sie die Attributsammlung der Schaltfläche für die Überschreibung ihres OnClick-Ereignisses verwenden müssen.

{{% alert color="primary" %}} 

Das ASP.NET-Schaltflächen-Steuerelement ist ein Serversteuerelement. Bei jedem Klicken wird ein serverseitiges Ereignis ausgelöst, aber wenn Sie dieses Schaltflächen-Steuerelement verwenden möchten, um auf der Clientseite einige Codes auszuführen (normalerweise unter Verwendung von Javascript), müssen Sie das onclick-Attribut unter dem Page_Load-Ereignis ändern. Aspose.Cells.GridWeb bietet einige Funktionen, die in Javascript aufgerufen werden können, um mit dem GridWeb-Steuerelement auf der Clientseite umzugehen. Im folgenden Beispiel haben wir die Funktionen updateData & validateAll (die clientseitige Funktionen sind) von GridWeb verwendet, um Griddaten zu aktualisieren und zu validieren.

{{% /alert %}} 
#### **Codebeispiel**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-UsingCommonSubmitButton.aspx-UsingCommonSubmitButton.cs" >}}
### **3. Ausführen der Anwendung**
Jetzt können Sie Ihre Anwendung kompilieren und ausführen, indem Sie Strg+F5 drücken, und die Seite wird in einem neuen Browserfenster geöffnet. Fügen Sie einige Werte zu GridWeb hinzu und drücken Sie auf die Schaltfläche Griddaten an Server übermitteln, und Sie werden feststellen, dass ein Postback durchgeführt wird, um GridWeb-Daten zu aktualisieren und zu validieren.
## **Fazit**
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb bietet eine hohe Flexibilität beim Arbeiten mit GridWeb-Steuerungen sowohl auf Server- als auch auf Clientseite. Entwickler haben zahlreiche Optionen, um die GridWeb-Steuerung in verschiedenen Szenarien zu verwenden und bessere Lösungen für ihre Kunden anzubieten.

{{% /alert %}}
