---
title: Arbeiten mit GridWeb
type: docs
weight: 20
url: /de/java/working-with-gridweb/
---

## **Öffnen einer Microsoft Excel-Datei**

Die Aspose.Cells.GridWeb-Steuerung kann Microsoft Excel-Dateien öffnen und laden, inklusive Daten, Formatierungen, Diagrammen, Bildern usw. Dieser Abschnitt erläutert wie.

Um eine Excel-Datei mithilfe der GridWeb-Steuerung zu öffnen:

1. Fügen Sie das Aspose.Cells.GridWeb-Steuerelement einem Webformular oder einer Seite hinzu.
1. Importieren Sie die Excel-Datei, indem Sie den Dateipfad angeben.
1. Starten Sie die Anwendung oder öffnen Sie die Seite.

Um den Inhalt aus einer Excel-Datei in die Aspose.Cells.GridWeb-Steuerung zu laden, müssen Sie die importExcelFile-Methode aufrufen, um den Pfad der Excel-Datei anzugeben. Danach findet die GridWeb-Steuerung automatisch die Datei im angegebenen Pfad und zeigt deren Inhalt an. Ein Code-Ausschnitt, der den Inhalt einer Excel-Datei lädt, wird unten bereitgestellt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-OpeningfromFile-OpeningfromFile.jsp" >}}

Der obenstehende Code-Ausschnitt kann auf beliebige Weise verwendet werden. Fügen Sie beispielsweise diesen Code zum Page_Load-Ereignis des Formulars hinzu, das Sie selbst spezifiziert haben, um automatisch eine Excel-Datei zu laden.

**Eine Excel-Datei wird in GridWeb geladen**

![todo:image_alt_text](working-with-gridweb_1.png)

## **Speichern einer Microsoft Excel-Datei**

Es ist möglich, neue oder vorhandene Microsoft Excel-Dateien auf Websites im GUI-Modus mithilfe der Aspose.Cells.GridWeb-Steuerung zu erstellen oder zu bearbeiten. Die Dateien können dann in Excel-Dateien gespeichert werden. Aspose.Cells.GridWeb fungiert effektiv als Online-Tabellenkalkulations-Editor. Dieser Abschnitt beschreibt, wie Gitterinhalt in Excel-Dateien gespeichert werden kann.

### **Als Datei speichern**

Um den Inhalt der Aspose.Cells.GridWeb-Steuerelement als Excel-Datei zu speichern:

1. Fügen Sie das Aspose.Cells.GridWeb-Steuerelement einem Webformular oder einer Seite hinzu.
1. Speichern Sie Ihre Arbeit als Excel-Datei an einem bestimmten Pfad.
1. Starten Sie die Anwendung oder öffnen Sie die Seite.

Das untenstehende Codebeispiel zeigt, wie der Inhalte des Gitters in eine Excel-Datei gespeichert werden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-SavingasFile-SavingasFile.jsp" >}}

Der obige Code-Schnipsel kann auf verschiedene Arten verwendet werden. Eine häufige Methode besteht darin, eine Schaltfläche hinzuzufügen, die den Gitterinhalt in eine Excel-Datei speichert, wenn darauf geklickt wird. Aspose.Cells.GridWeb bietet einen einfacheren Ansatz für diese Aufgabe. Aspose.Cells.GridWeb verfügt über ein Ereignis namens SaveCommand. Der obige Code-Schnipsel kann dem Ereignishandler des SaveCommand-Ereignisses hinzugefügt werden, der es Benutzern ermöglicht, ihre Arbeit durch Klicken auf die integrierte **Speichern**-Schaltfläche von Aspose.Cells.GridWeb zu speichern.

## **Ändern der Größe von Aspose.Cells.GridWeb und seiner Kopfleiste**

In diesem Artikel erfahren Sie, wie Sie mithilfe der Aspose.Cells.GridWeb-API das GridWeb zur Laufzeit neu dimensionieren und die Kopfleiste des Aspose.Cells.GridWeb-Steuerelements neu dimensionieren, um die Daten leichter lesbar zu machen.

### **Ändern von Breite & Höhe von Aspose.Cells.GridWeb**

Die Änderung der Breite und Höhe des Aspose.Cells.GridWeb-Steuerelements ist eine einfache, aber wichtige Funktion. Das Aspose.Cells.GridWeb-Steuerelement wird durch die GridWeb-Klasse in der API dargestellt. Um die Breite und Höhe des GridWeb-Steuerelements zu ändern, verwenden Sie einfach seine Breiten- und Höheneigenschaften.

{{% alert color="primary" %}}

Die Breite und
Höhe des Steuerelements können in Pixel oder Punkten definiert werden.

{{% /alert %}}

Der Ausgabewert des folgenden Code-Schnipsels wird unten angezeigt.

**Geänderte Breite und Höhe des GridWeb-Steuerelements**

![todo:image_alt_text](working-with-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangedwidthheightofGridWebcontrol-ChangedwidthheightofGridWebcontrol.jsp" >}}

### **Ändern von Breite & Höhe der Kopfleiste**

Das Aspose.Cells.GridWeb-Steuerelement enthält zwei Kopfleisten wie folgt:

- Obere Kopfleiste, diese Kopfleiste stellt Spalten als A, B, C, D, usw. dar.
- Linke Kopfleiste, diese Kopfleiste stellt Zeilen als 1, 2, 3, 4, usw. dar.

Beide dieser Kopfleisten sind unten aufgeführt.

**Kopfleisten**

![todo:image_alt_text](working-with-gridweb_3.png)

Ändern Sie die Höhe der oberen Kopfzeile und die Breite der linken Kopfzeile mithilfe der Eigenschaften HeaderBarHeight und HeaderBarWidth des GridWeb-Steuerelements. Die Abbildung unten zeigt die Ausgabe des nachfolgenden Codebeispiels.

**Geänderte Kopfzeilenbreite und -höhe**

![todo:image_alt_text](working-with-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangingWidthandHeightofHeaderBar-ChangingWidthandHeightofHeaderBar.jsp" >}}

## **Arbeiten mit Aspose.Cells.GridWeb-Ereignissen**

Alle Entwickler müssen mit Ereignissen und ihrem Zweck vertraut sein. Ereignisse werden verwendet, um Benachrichtigungen über Änderungen zu senden, die in einem Steuerelement oder einer Klasse auftreten können. Aspose.Cells.GridWeb verfügt über mehrere Ereignisse, die verwendet werden können, um bestimmte Aufgaben auszuführen, wenn bestimmte Änderungen im Steuerelement auftreten.

Dieses Thema bietet eine Einführung in alle von Aspose.Cells.GridWeb-Steuerelement unterstützten Ereignisse sowie einige Details dazu, wie diese Ereignisse gehandhabt werden können.

### **Einführung in Grid-Ereignisse**

Das Aspose.Cells.GridWeb-Steuerelement unterstützt mehrere Ereignisse, die eine genauere Steuerung bei der Ausführung von Operationen ermöglichen, wenn bestimmte Ereignisse im Steuerelement ausgelöst werden. Eine vollständige Liste der von Aspose.Cells.GridWeb-Steuerelement unterstützten Ereignisse finden Sie unten.

|**Ereignisse**|**Beschreibung**|
| :- | :- |
|CellCommand| Tritt auf, wenn der Befehls-Hyperlink einer Zelle geklickt wird. Wenn dieses Ereignis ausgelöst wird, liefert sein Parameter e.Argument den Namen des Befehls.
|CellDoubleClick| Tritt auf, wenn die Zelle doppelgeklickt wird.
|ColumnDeleted| Tritt auf, wenn ein Benutzer eine Spalte aus einem Arbeitsblatt mithilfe des Client-Seitenmenüs löscht.
|ColumnDeleting| Tritt auf, wenn ein Benutzer versucht, eine Spalte aus einem Arbeitsblatt mithilfe des Client-Seitenmenüs zu löschen.
|ColumnDoubleClick| Tritt auf, wenn auf die Spaltenüberschrift doppelgeklickt wird.
|ColumnInserted| Tritt auf, wenn ein Benutzer mithilfe des Client-Seitenmenüs eine Spalte in ein Arbeitsblatt einfügt.
|CustomCommand| Tritt auf, wenn ein Benutzer auf eine benutzerdefinierte Befehlsschaltfläche klickt.
|LoadCustomData| Tritt auf, wenn die Eigenschaft EnableSession des Steuerelements auf false gesetzt ist und Arbeitsblattdaten geladen werden müssen. In einer sitzungslosen Sitzung können Sie dieses Ereignis handhaben, um Arbeitsblattdaten aus einer Datei oder einer Datenbank zu laden.
|PageIndexChanged| Tritt auf, wenn der Blattseitenindex des Steuerelements geändert wird.
|RowDeleted| Tritt auf, wenn ein Benutzer eine Zeile aus dem Arbeitsblatt mithilfe des Client-Seitenmenüs löscht.
|RowDeleting| Tritt auf, wenn ein Benutzer versucht, eine Zeile aus einem Arbeitsblatt mithilfe des Client-Seitenmenüs zu löschen.
|RowDoubleClick| Tritt auf, wenn auf die Zeilenüberschrift doppelgeklickt wird.
|RowInserted|Tritt auf, wenn ein Benutzer eine Zeile in das Arbeitsblatt über das clientseitige Menü einfügt.
|SaveCommand|Tritt auf, wenn auf die **Speichern**-Schaltfläche geklickt wird.
|SheetTabClick|Tritt auf, wenn auf eine Blattregisterkarte geklickt wird.
|SubmitCommand|Tritt auf, wenn auf die **Senden**-Schaltfläche geklickt wird.
|UndoCommand|Tritt auf, wenn auf die **Rückgängig**-Schaltfläche geklickt wird.
|AjaxCallFinished|Wird ausgelöst, wenn die AJAX-Aktualisierung des Steuerelements abgeschlossen ist. (EnableAJAX muss auf true gesetzt sein).
|CellModifiedOnAjax|Wird ausgelöst, wenn die Zelle in einem AJAX-Aufruf geändert wird.
|AfterColumnFilter|Wird ausgelöst, wenn ein Filter auf eine Spalte angewendet wird.

### **Behandlung von Grid-Ereignissen**

Um eine bestimmte Operation bei Auslösung eines bestimmten Ereignisses durchzuführen, muss ein Ereignishandler erstellt werden. Ein Ereignishandler führt die gewünschte Aufgabe aus, wenn ein bestimmtes Ereignis ausgelöst wird. Das folgende Beispiel zeigt, wie mit einem einfachen Grid-Ereignis umgegangen werden kann.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HandlingGridEvents-HandlingGridEvents.jsp" >}}

## **Arbeiten mit Double-Click-Ereignissen**

Aspose.Cells.GridWeb enthält drei Arten von Double-Click-Ereignissen:

- CellDoubleClick, ausgelöst, wenn auf eine Zelle doppelgeklickt wird.
- ColumnDoubleClick, ausgelöst, wenn auf eine Spaltenüberschrift doppelgeklickt wird.
- RowDoubleClick, ausgelöst, wenn auf eine Zeilenüberschrift doppelgeklickt wird.

In diesem Thema wird erläutert, wie Double-Click-Ereignisse in Aspose.Cells.GridWeb aktiviert werden können. Es wird auch die Erstellung von Ereignishandlern für diese Ereignisse erläutert.

### **Aktivieren von Double-Click-Ereignissen**

Alle Arten von Double-Click-Ereignissen können clientseitig aktiviert werden, indem die Eigenschaft EnableDoubleClickEvent des GridWeb-Steuerelements auf true gesetzt wird.

{{% alert color="primary" %}}

Standardmäßig ist die Eigenschaft EnableDoubleClickEvent auf false gesetzt. Dies bedeutet, dass Double-Click-Ereignisse standardmäßig nicht aktiviert sind. Um solche Ereignisse zu implementieren, muss zunächst die Funktion aktiviert werden.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-EnablingDoubleClickEvents-EnablingDoubleClickEvents.jsp" >}}

Sobald Double-Click-Ereignisse aktiviert sind, ist es möglich, Ereignishandler für jedes Double-Click-Ereignis zu erstellen. Diese Ereignishandler führen spezifische Aufgaben aus, wenn ein bestimmtes Double-Click-Ereignis ausgelöst wird.

### **Behandlung von Doppelklickereignissen**

#### **Zelle doppelklicken**

Der Ereignisbehandlungsroutinen für das CellDoubleClick-Ereignis stellt ein Argument vom Typ CellEventArgs bereit, das die vollständigen Informationen über die Zelle liefert, die doppelgeklickt wurde.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickCell-DoubleClickCell.jsp" >}}

#### **Spaltenkopf doppelklicken**

Der Ereignisbehandlungsroutinen für das ColumnDoubleClick-Ereigniss stellt ein Argument vom Typ RowColumnEventArgs bereit, das die Indexnummer der Spalte für den doppelgeklickten Kopf sowie andere Informationen liefert.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickColumnHeader-DoubleClickColumnHeader.jsp" >}}

#### **Zeilenkopf doppelklicken**

Der Ereignisbehandilungsroutinen für das RowDoubleClick-Ereignis stellt ein Argument vom Typ RowColumnEventArgs bereit, das die Indexnummer der Reihe für den doppelgeklickten Kopf sowie andere relevante Informationen liefert.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickRowHeader-DoubleClickRowHeader.jsp" >}}

## **Stil oder Erscheinung von Aspose.Cells.GridWeb festlegen**

Aspose.Cells.GridWeb hat sein eigenes Standardaussehen, aber es ist möglich, sein Erscheinungsbild zu ändern. Aspose.Cells.GridWeb bietet mehrere Eigenschaften, um Entwicklern die vollständige Kontrolle über sein Aussehen zu ermöglichen. Dieses Thema erörtert einige dieser Eigenschaften.

### **Stil oder Erscheinung von Aspose.Cells.GridWeb festlegen**

#### **Voreingestellte Stile**

Um den Aufwand der Entwickler zu reduzieren, bietet Aspose.Cells.GridWeb einige voreingestellte Stile an. Wählen Sie einfach einen Stil aus der Liste aus, um ihn anzuwenden.

|**Stile**|**Farbschema**|
| :- | :- |
|Standard|Silver|
|Colorful1|Rose|
|Colorful2|Blue|
|Professional1|Cyan|
|Professional2|Cyan again|
|Traditional1|Dark|
|Traditional2|Gray|
|Custom|Customized|
Wenn ein bestimmter Stil ausgewählt wird, ändert dies das gesamte Erscheinungsbild der GridWeb-Steuerung. Entwickler können einen voreingestellten Stil auswählen, der zur Laufzeit mittels der flexiblen API von Aspose.Cells.GridWeb angewendet wird.

Die GridWeb-Steuerung bietet die Eigenschaft PresetStyle, der Entwickler einen beliebigen voreingestellten Stil zuweisen können.

Der Ausgang des folgenden Code-Schnipsels wird unten angezeigt.

**GridWeb-Steuerung mit angewendetem Colorful1-Stil**

![todo:image_alt_text](working-with-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **Kopfzeilen-Stil**

Wenn Sie sich die GridWeb-Steuerung ansehen, werden Sie zwei Kopfzeilen bemerken. Eine für Spalten (das ist A, B, C, D usw.) und die andere für Zeilen (das ist 1, 2, 3, 4, usw.). Aspose.Cells.GridWeb ermöglicht es Entwicklern, das Erscheinungsbild dieser Kopfzeilen zu kontrollieren. Entwickler können das Erscheinungsbild der Kopfzeilen zur Laufzeit festlegen.

{{% alert color="primary" %}}

Die GridWeb-Steuerung bietet die Eigenschaft HeaderBarStyle, die einen Stil auf beide Kopfzeilen der Steuerung anwendet.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **Tab-Leistenstil**

Es ist auch möglich, den Stil der Registerkarte festzulegen. Bitte beachten Sie den folgenden Code.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HeaderBarStyle-HeaderBarStyle.jsp" >}}

#### **Stil-Datei laden**

Um Stil-Einstellungen aus einer vorhandenen Stil-Datei auf das GridWeb-Steuerelement anzuwenden, können Entwickler den Pfad der Stil-Datei auf die Eigenschaft CustomStyleFileName des Steuerelements setzen. Bevor dies jedoch geschieht, muss die Eigenschaft PresetStyle des Steuerelements auf Benutzerdefiniert gesetzt werden. Das liegt daran, dass die Stil-Datei benutzerdefinierte Stilinformationen enthält, die bereits von einem Entwickler definiert wurden.

Bitte beachten Sie das folgende Bild, das GridWeb mit dem angewendeten benutzerdefinierten Stil zeigt.

![todo:image_alt_text](working-with-gridweb_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-CustomStyleSheet-CustomStyleSheet.jsp" >}}

{{% alert color="primary" %}}

WICHTIG: Das Laden einer Stil-Datei in das GridWeb-Steuerelement hat keine Auswirkungen auf die Formatierungseinstellungen der Zellen des Steuerelements.

{{% /alert %}}

#### **Beispiel für benutzerdefiniertes Stil-Template**

Hier ist das Beispiel für das benutzerdefinierte Stil-Template. Sie können es entsprechend Ihren Anforderungen anpassen.

{{< highlight java >}}

 <aspose.excel.web.viewerStyletemplate runat="server" HeaderBarWidth="30pt" ScrollBarBaseColor="#AFEEEE" SelectCellBgColor="#FFFAF0" ActiveHeaderBgColor="#DAA520" ActiveCellBgColor="#DDDDFF" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LeftBorderStyle-BorderWidth="" FrameTableStyle-LeftBorderStyle-BorderColor="" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-RightBorderStyle-BorderWidth="" FrameTableStyle-RightBorderStyle-BorderColor="" FrameTableStyle-BorderWidth="1px" FrameTableStyle-CellSpacing="0" FrameTableStyle-BorderColor="#C0FFC0" FrameTableStyle-CellPadding="0" FrameTableStyle-TopBorderStyle-BorderWidth="" FrameTableStyle-TopBorderStyle-BorderColor="" FrameTableStyle-BackColor="#FFFFCC" FrameTableStyle-BottomBorderStyle-BorderWidth="" FrameTableStyle-BottomBorderStyle-BorderColor="" HeaderBarStyle-LeftBorderStyle-BorderWidth="" HeaderBarStyle-LeftBorderStyle-BorderColor="" HeaderBarStyle-verticalalign="Middle" HeaderBarStyle-RightBorderStyle-BorderWidth="" HeaderBarStyle-RightBorderStyle-BorderColor="" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-font-size="10pt" HeaderBarStyle-BorderColor="#00C0C0" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-horizontalalign="Center" HeaderBarStyle-ForeColor="Red" HeaderBarStyle-TopBorderStyle-BorderWidth="" HeaderBarStyle-TopBorderStyle-BorderColor="" HeaderBarStyle-BackColor="#D8BFD8" HeaderBarStyle-BottomBorderStyle-BorderWidth="" HeaderBarStyle-BottomBorderStyle-BorderColor="" ViewTableStyle-LeftBorderStyle-BorderWidth="" ViewTableStyle-LeftBorderStyle-BorderColor="" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-RightBorderStyle-BorderWidth="" ViewTableStyle-RightBorderStyle-BorderColor="" ViewTableStyle-BorderWidth="0px" ViewTableStyle-CellSpacing="0" ViewTableStyle-CellPadding="0" ViewTableStyle-TopBorderStyle-BorderWidth="" ViewTableStyle-TopBorderStyle-BorderColor="" ViewTableStyle-BottomBorderStyle-BorderWidth="" ViewTableStyle-BottomBorderStyle-BorderColor="" BottomTableStyle-LeftBorderStyle-BorderWidth="" BottomTableStyle-LeftBorderStyle-BorderColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-RightBorderStyle-BorderWidth="" BottomTableStyle-RightBorderStyle-BorderColor="" BottomTableStyle-Height="32pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-CellSpacing="0" BottomTableStyle-BorderColor="#80FF80" BottomTableStyle-CellPadding="0" BottomTableStyle-ForeColor="#FFE0C0" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="#FF69B4" BottomTableStyle-BottomBorderStyle-BorderWidth="" BottomTableStyle-BottomBorderStyle-BorderColor="" HeaderBarHeight="15pt" ActiveTabStyle-LeftBorderStyle-BorderWidth="" ActiveTabStyle-LeftBorderStyle-BorderColor="" ActiveTabStyle-RightBorderStyle-BorderWidth="" ActiveTabStyle-RightBorderStyle-BorderColor="" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-font-size="10pt" ActiveTabStyle-BorderColor="#00C0C0" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="#FF00FF" ActiveTabStyle-TopBorderStyle-BorderWidth="" ActiveTabStyle-TopBorderStyle-BorderColor="" ActiveTabStyle-BackColor="#80FFFF" ActiveTabStyle-BottomBorderStyle-BorderWidth="" ActiveTabStyle-BottomBorderStyle-BorderColor="" HeaderBarTableStyle-LeftBorderStyle-BorderWidth="" HeaderBarTableStyle-LeftBorderStyle-BorderColor="" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-RightBorderStyle-BorderWidth="" HeaderBarTableStyle-RightBorderStyle-BorderColor="" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-CellSpacing="0" HeaderBarTableStyle-CellPadding="0" HeaderBarTableStyle-TopBorderStyle-BorderWidth="" HeaderBarTableStyle-TopBorderStyle-BorderColor="" HeaderBarTableStyle-BackColor="#C0FFC0" HeaderBarTableStyle-BottomBorderStyle-BorderWidth="" HeaderBarTableStyle-BottomBorderStyle-BorderColor="" DefaultGridLineColor="#228B22" TabStyle-LeftBorderStyle-BorderWidth="" TabStyle-LeftBorderStyle-BorderColor="" TabStyle-RightBorderStyle-BorderWidth="" TabStyle-RightBorderStyle-BorderColor="" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-font-size="8pt" TabStyle-BorderColor="#8080FF" TabStyle-BorderStyle="Groove" TabStyle-ForeColor="#FFFFCC" TabStyle-TopBorderStyle-BorderWidth="" TabStyle-TopBorderStyle-BorderColor="" TabStyle-BackColor="#C0C0FF" TabStyle-BottomBorderStyle-BorderWidth="" TabStyle-BottomBorderStyle-BorderColor="" scrollbararrowColor="#778899"/>

{{< /highlight >}}

## **Steuerung auf einem Webformular erstellen**

In diesem Artikel erfahren Sie, wie Sie ein einfaches Webformular JSP (Java Server Page) erstellen, das das GridWeb-Steuerelement enthält.

**Schritt 1 - Verzeichnisstruktur erstellen**

Sie müssen die folgende Verzeichnisstruktur im Verzeichnis **webapps** des Tomcat-Servers erstellen

![todo:image_alt_text](working-with-gridweb_7.png)

Das sind die Verzeichnisse und Dateien, die Sie erstellen müssen. Bitte lesen Sie die Kommentare und folgen Sie ihnen. Sie können die neuesten Aspose.Cells.GridWeb für Java Release-Archive von [diesem Link](https://downloads.aspose.com/cells/java) erhalten.

{{< highlight java >}}

 SamplePageGridWebJava

SamplePageGridWebJava\grid

//Get acwclient directory from GridWeb latest release archive from Downloads section

SamplePageGridWebJava\acwclient

SamplePageGridWebJava\WEB-INF

SamplePageGridWebJava\WEB-INF\lib

//Get aspose-gridweb-x.x.x.jar file from GridWeb latest release archive from Downloads section

SamplePageGridWebJava\WEB-INF\aspose-gridweb-x.x.x.jar

SamplePageGridWebJava\WEB-INF\web.xml

SamplePageGridWebJava\head.jsp

//Create this excel file using Microsoft Excel or you can use any excel file and rename it SampleExcel.xlsx

SamplePageGridWebJava\SampleExcel.xlsx

SamplePageGridWebJava\SamplePage.jsp

{{< /highlight >}}

**Schritt 2 - Codes in erstellte Dateien hinzufügen**

In diesem Abschnitt wird der Code für verschiedene Dateien erstellt, die in der obigen Verzeichnisstruktur erstellt wurden. Bitte holen Sie sich diese Codes und fügen Sie sie in Ihre Dateien ein, indem Sie sie in Notepad öffnen und sie kopieren/einfügen.

**Web.xml**

{{< highlight java >}}

 <?xml version="1.0" encoding="UTF-8"?>

<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://java.sun.com/xml/ns/javaee" xmlns:web="http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd" xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd" id="WebApp_ID" version="2.5">

  <display-name>testGridWeb</display-name>

  <welcome-file-list>

    <welcome-file>SamplePage.jsp</welcome-file>

  </welcome-file-list>

  <servlet>

    <display-name>GridWebServlet</display-name>

    <servlet-name>GridWebServlet</servlet-name>

    <servlet-class>com.aspose.gridweb.GridWebServlet</servlet-class>

  </servlet>

  <servlet-mapping>

    <servlet-name>GridWebServlet</servlet-name>

    <url-pattern>/GridWebServlet</url-pattern>

  </servlet-mapping>

</web-app>

{{< /highlight >}}

**head.jsp**

{{< highlight java >}}

 <%

String path = request.getContextPath();

String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";

%>

<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE9"/>

<base href="<%=basePath%>">

<script type="text/javascript" language="javascript"

	src="grid/acw_client/acwmain.js"></script>

<script type="text/javascript" language="javascript"

	src="grid/acw_client/lang_en.js"></script>

<link href="grid/acw_client/menu.css" rel="stylesheet" type="text/css" />

<style>

span.acwxc {

	overflow: hidden;

	border: none;

	display: block;

	white-space: pre;

}

</style>

<style>

span.rotation90 {

	width: 100%;

	height: 100%;

	border: none;

	-webkit-transform: rotate(-90deg);

	-moz-transform: rotate(-90deg);

	filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=3 );

	display: block

}

</style>

<style>

span.rotation-90 {

	filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=1 );

	width: 100%;

	height: 100%;

	border: none;

	-webkit-transform: rotate(90deg);

	-moz-transform: rotate(90deg);

	display: block

}

</style>

<style>

span.wrap {

	white-space: pre-wrap;

	white-space: -moz-pre-wrap;

	white-space: -pre-wrap;

	white-space: -o-pre-wrap;

	word-wrap: break-word;

	-ms-word-break: break-all;

}

</style>

{{< /highlight >}}

**SamplePage.jsp**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-SamplePage-SamplePage.jsp" >}}

**Schritt 3 - Ausführen Ihrer Beispiel-JSP-Webseite**

Jetzt haben Sie alles erledigt. Es ist an der Zeit, die Webseite auszuführen. Starten Sie bitte Ihren Tomcat-Server und fügen Sie dann die folgende URL in den Webbrowser ein.

{{< highlight java >}}

 http://localhost:8080/SamplePageGridWebJava/SamplePage.jsp

{{< /highlight >}}

Sie werden etwas Ähnliches wie den folgenden Screenshot sehen. Herzlichen Glückwunsch, Sie haben die GridWeb-Steuerung erfolgreich auf Ihrer JSP-Seite verwendet.

![todo:image_alt_text](working-with-gridweb_8.png)

## **GridWeb drucken**

Es gibt Zeiten, in denen Entwickler den Inhalt des GridWeb von einer Webseite drucken müssen, ohne eine Microsoft Excel-Datei zu speichern. Die Aspose.Cells.GridWeb-Steuerung unterstützt diese Funktion.

### **GridWeb drucken**

Um ohne separate Dateispeicherung zu drucken, rufen Sie die print()-Methode der GridWeb-Klasse clientseitig auf, um das Raster zu drucken. Sie können auch ein geeignetes Ereignis auswählen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-PrintingGridWeb-PrintingGridWeb.jsp" >}}

Da Sie es vom Client aus aufrufen, müssen Sie zuerst die Client-ID des GridWeb abrufen. Sie können die Client-ID mit der Methode gridweb.getClientID() abrufen.

### **Beispielcode auf der Clientseite**

Bitte sehen Sie sich den folgenden Link an, der die Methode gridweb.print() von der Clientseite aufruft.

**HTML**

{{< highlight java >}}

 <a href="#" onclick='<%=gridweb.getClientID()%>.print(); '>Print Function of GridWeb</a>

{{< /highlight >}}

## **Einführung in verschiedene Rastermodi**

Dieser Artikel beschreibt die verschiedenen Modi von Aspose.Cells.GridWeb. Diese Modi unterscheiden sich logisch aufgrund ihrer unterschiedlichen Funktionen und Verhaltensweisen. Wir haben verschiedene Arten von Modi identifiziert:

- Bearbeitungsmodus
- Anzeigemodus

Jeder dieser Modi hat seine eigenen Merkmale. Entwickler können mit Aspose.Cells.GridWeb in jedem Modus gemäß ihren Anforderungen arbeiten. Wir werden uns jeden Modus unten genauer ansehen.

### **Bearbeitungsmodus**

Standardmäßig ist die Aspose.Cells.GridWeb-Steuerung im Bearbeitungsmodus. Im Bearbeitungsmodus können Sie den Rasterinhalt vollständig bearbeiten oder modifizieren und dabei alle Funktionen der Aspose.Cells.GridWeb-Steuerung nutzen. Zu diesen Funktionen gehören:

- Speichern des Rasterinhalts in Microsoft Excel-Dateien.
- Übermittlung von Daten an einen Server.
- Berechnung von Formeln.
- Rückgängigmachen oder Verwerfen früherer Aktionen.
- Verwalten von Zeilen und Spalten.
- Ausschneiden, Kopieren oder Einfügen von Daten.
- Formatieren von Zellen usw.

**GridWeb Steuerelement im Bearbeitungsmodus**

![todo:image_alt_text](working-with-gridweb_9.png)

Entwickler können auch programmgesteuert in den Bearbeitungsmodus wechseln, indem sie die EditMode-Eigenschaft des GridWeb-Steuerelements auf true setzen.

### **Codebeispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebEditMode-GridWebEditMode.jsp" >}}

### **Anzeigemodus**

Wenn das GridWeb-Steuerelement im Anzeigemodus ist, können Benutzer den Rasterinhalt nicht bearbeiten oder ändern, das bedeutet, dass Benutzer nur den Rasterinhalt anzeigen können. Aus diesem Grund wird dieser Modus Anzeigemodus genannt. Im Anzeigemodus sind einige Schaltflächen (**Senden**, **Speichern** und **Rückgängig**) ausgeblendet und das Menü, das beim Rechtsklicken erscheint, enthält nur die Optionen **Kopieren** und **Suchen**.

**GridWeb Steuerelement im Anzeigemodus** 

![todo:image_alt_text](working-with-gridweb_10.png)

Wenn Entwickler möchten, dass ihre Benutzer nur Daten anzeigen können, können sie programmgesteuert in den Anzeigemodus wechseln, indem sie die EditMode-Eigenschaft des GridWeb-Steuerelements auf **false** setzen.

### **Codebeispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebViewMode-GridWebViewMode.jsp" >}}

{{% alert color="primary" %}}

Auch im Anzeigemodus können Benutzer die Höhe und Breite von Zeilen und Spalten ändern.

{{% /alert %}}
