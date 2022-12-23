---
title: Verwenden einer gemeinsamen Schaltfläche zum Senden von Rasterdaten
type: docs
weight: 20
url: /de/net/using-a-common-button-to-submit-grid-data/
---
{{% alert color="primary" %}} 

 Aspose.Cells.GridWeb bietet einige integrierte Befehlsschaltflächen wie**einreichen** und**Speichern**. Verwenden Sie diese Schaltflächen, um verwandte Aufgaben auszuführen.

In diesem Artikel wird gezeigt, wie Sie Daten an einen Server übermitteln, indem Sie nicht nur auf die integrierte GridWeb klicken**Speichern** Befehlsschaltfläche, sondern durch Klicken auf eine allgemeine ASP.NET-Schaltfläche (Websteuerung). Der Zweck dieses Artikels besteht darin, die Flexibilität von Aspose.Cells.GridWeb zu zeigen. Darüber hinaus verwendet dieser Artikel auch spezielle Funktionen, die von Aspose.Cells.GridWeb verfügbar gemacht werden, um im clientseitigen Skript verwendet zu werden.

{{% /alert %}} 
## **Übermitteln von Rasterdaten mithilfe einer ASP.NET-Schaltfläche**
Aspose.Cells.GridWeb bietet drei integrierte Schaltflächen (**einreichen**, **Speichern** und**Rückgängig machen** ). Nach der Bearbeitung in GridWeb kann ein Benutzer auf die klicken**einreichen** oder**Speichern** Schaltfläche in der Registerkartenleiste, damit GridWeb Daten an den Server senden kann. Wenn der Benutzer auf eine Blattregisterkarte klickt, führt das GridWeb-Steuerelement dieselbe Aufgabe aus wie die integrierten Befehlsschaltflächen. Aspose.Cells. GridWeb unterstützt auch das Hinzufügen dieser Funktionalität zu einem allgemeinen ASP.NET Button-Steuerelement, aber Sie müssen der Anwendung zusätzlichen Code hinzufügen.
### **1. Erstellen einer Testanwendung**
Öffnen Sie Ihre Visual Studio.NET-IDE und erstellen Sie ein neues ASP.NET-Webanwendungsprojekt. Nachdem die Anwendung erstellt wurde, wird Ihrem Projekt eine Standardseite „WebForm1.aspx“ hinzugefügt. Ziehen Sie das GridWeb-Steuerelement per Drag & Drop aus Ihrer Toolbox in das Web Form. Wenn Sie das GridWeb-Steuerelement nicht in Ihrer Toolbox finden können, lesen Sie diese Seite:[Integrieren Sie Aspose.Cells-Rastersteuerelemente in Visual Studio.NET](/cells/de/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/) um mehr darüber zu erfahren. Nachdem das GridWeb-Steuerelement zu Ihrem Webformular hinzugefügt wurde, fügen Sie Ihrem Webformular auch ein Schaltflächen-Websteuerelement aus der Toolbox hinzu.
### **2. Hinzufügen von Code zum Page_Load-Ereignis**
Jetzt ist es an der Zeit, Page etwas Code hinzuzufügen_Load-Event des Web Forms. Sie können in der Entwurfsansicht auf das Webformular doppelklicken und die VS.NET IDE bringt Sie automatisch zur Seite_Laden Sie den Ereignishandler, bei dem Sie die Attributes-Sammlung des Buttons verwenden müssten, um sein OnClick-Ereignis zu überschreiben.

{{% alert color="primary" %}} 

ASP.NET Das Schaltflächen-Steuerelement ist ein serverseitiges Steuerelement. Jedes Mal, wenn darauf geklickt wird, wird ein serverseitiges Ereignis ausgelöst, aber wenn Sie dieses Schaltflächen-Steuerelement verwenden möchten, um Code auf der Client-Seite auszuführen (normalerweise mit Javascript), dann müssen Sie sein onclick-Attribut unter dem Page_Load-Ereignis ändern. Aspose.Cells.GridWeb bietet einige Funktionen, die in Javascript aufgerufen werden können, um die GridWeb-Steuerung von der Client-Seite zu handhaben. Im folgenden Beispiel haben wir die Funktionen updateData & validateAll (die clientseitigen Funktionen sind) von GridWeb verwendet, um Grid-Daten zu aktualisieren und zu validieren.

{{% /alert %}} 
#### **Codebeispiel**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-UsingCommonSubmitButton.aspx-UsingCommonSubmitButton.cs" >}}
### **3. Ausführen der Anwendung**
Jetzt können Sie Ihre Anwendung kompilieren und ausführen, indem Sie Strg+F5 drücken, und die Seite wird in einem neuen Browserfenster geöffnet. Lassen Sie uns einige Werte zu GridWeb hinzufügen und auf die Schaltfläche „Grid-Daten an Server senden“ klicken, und Sie würden sehen, dass ein Postback auftritt, um GridWeb-Daten zu aktualisieren und zu validieren.
## **Fazit**
{{% alert color="primary" %}} 

Aspose.Cells. GridWeb bietet eine große Flexibilität für die Arbeit mit GridWeb-Steuerelementen auf Server- oder Clientseite. Entwickler haben eine Vielzahl von Optionen, um das GridWeb-Steuerelement in verschiedenen Arten von Szenarien zu verwenden, um ihren Kunden bessere Lösungen anzubieten.

{{% /alert %}}
