---
title: Arbeiten mit GridWeb
type: docs
weight: 20
url: /de/java/working-with-gridweb/
---
## **Öffnen einer Microsoft Excel-Datei**

Aspose.Cells. Das GridWeb-Steuerelement kann Microsoft Excel-Dateien öffnen und laden – komplett mit Daten, Formatierungen, Diagrammen, Bildern usw. In diesem Thema wird erläutert, wie.

So öffnen Sie eine Excel-Datei mit dem GridWeb-Steuerelement:

1. Fügen Sie das Steuerelement Aspose.Cells.GridWeb einem Webformular oder einer Seite hinzu.
1. Importieren Sie die Excel-Datei, indem Sie den Dateipfad angeben.
1. Führen Sie die Anwendung aus oder öffnen Sie die Seite.

Um den Inhalt aus einer Excel-Datei in das Aspose.Cells.GridWeb-Steuerelement zu laden, müssen Sie die Methode importExcelFile aufrufen, um den Pfad der Excel-Datei anzugeben. Danach findet das GridWeb-Steuerelement automatisch die Datei aus dem angegebenen Pfad und zeigt ihren Inhalt darin an. Unten finden Sie ein Code-Snippet, das den Inhalt einer Excel-Datei lädt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-OpeningfromFile-OpeningfromFile.jsp" >}}

Das obige Code-Snippet kann beliebig verwendet werden. Um beispielsweise eine Excel-Datei automatisch zu laden, wenn ein Webformular geladen wird, fügen Sie diesen Code zum Page_Load-Ereignis des Formulars hinzu, das Sie selbst angegeben haben.

**Eine Excel-Datei wird in GridWeb geladen**

![todo: Bild_alt_Text](working-with-gridweb_1.png)

## **Speichern einer Microsoft Excel-Datei**

Es ist möglich, neue Microsoft Excel-Dateien zu erstellen oder vorhandene zu manipulieren, auf Websites im GUI-Modus unter Verwendung des Aspose.Cells.GridWeb-Steuerelements. Die Dateien können dann in Excel-Dateien gespeichert werden. Aspose.Cells.GridWeb dient effektiv als Online-Tabellenkalkulationseditor. In diesem Thema wird beschrieben, wie Rasterinhalte in Excel-Dateien gespeichert werden.

### **Als Datei speichern**

So speichern Sie den Inhalt des Steuerelements Aspose.Cells.GridWeb als Excel-Datei:

1. Fügen Sie das Steuerelement Aspose.Cells.GridWeb einem Webformular oder einer Seite hinzu.
1. Speichern Sie Ihre Arbeit als Excel-Datei unter einem angegebenen Pfad.
1. Führen Sie die Anwendung aus oder öffnen Sie die Seite.

Das folgende Codebeispiel veranschaulicht, wie Rasterinhalte in einer Excel-Datei gespeichert werden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-SavingasFile-SavingasFile.jsp" >}}

 Das obige Code-Snippet kann auf verschiedene Weise verwendet werden. Eine gängige Methode besteht darin, eine Schaltfläche hinzuzufügen, die den Rasterinhalt in einer Excel-Datei speichert, wenn darauf geklickt wird. Aspose.Cells. GridWeb bietet einen einfacheren Ansatz für die Aufgabe. Aspose.Cells.GridWeb hat ein Ereignis namens SaveCommand. Der obige Codeausschnitt kann dem Ereignishandler des SaveCommand-Ereignisses hinzugefügt werden, wodurch Benutzer ihre Arbeit speichern können, indem sie auf das integrierte Aspose.Cells.GridWeb klicken**Speichern** Taste.

## **Größenänderung von Aspose.Cells.GridWeb und seiner Kopfleiste**

In diesem Artikel wird erläutert, wie Sie GridWeb zur Laufzeit mithilfe von Aspose.Cells.GridWeb API in der Größe ändern. Außerdem wird erläutert, wie Sie die Größe der Kopfleisten des Aspose.Cells.GridWeb-Steuerelements ändern, um ihre Daten leichter lesbar zu machen.

### **Breite und Höhe von Aspose.Cells.GridWeb ändern**

Das Ändern der Breite und Höhe des Aspose.Cells.GridWeb-Steuerelements ist eine einfache, aber wichtige Funktion. Das Aspose.Cells.GridWeb-Steuerelement wird durch die GridWeb-Klasse in API dargestellt. Um die Breite und Höhe des GridWeb-Steuerelements zu ändern, verwenden Sie einfach seine Breiten- und Höheneigenschaften.

{{% alert color="primary" %}}

Breite und Höhe des Steuerelements können in Pixeln oder Punkten angegeben werden.

{{% /alert %}}

Die Ausgabe des folgenden Code-Snippets ist unten dargestellt.

**Geänderte Breite und Höhe des GridWeb-Steuerelements**

![todo: Bild_alt_Text](working-with-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangedwidthheightofGridWebcontrol-ChangedwidthheightofGridWebcontrol.jsp" >}}

### **Breite und Höhe der Kopfleiste ändern**

Aspose.Cells. Das GridWeb-Steuerelement enthält zwei Kopfleisten wie folgt:

- Obere Kopfleiste, diese Kopfleiste repräsentiert Spalten als A, B, C, D usw.
- Linke Kopfleiste, diese Kopfleiste stellt Zeilen als 1, 2, 3, 4 usw. dar.

Diese beiden Kopfleisten sind unten dargestellt.

**Kopfleisten**

![todo: Bild_alt_Text](working-with-gridweb_3.png)

Ändern Sie die Höhe der oberen Kopfleiste und die Breite der linken Kopfleiste mit den Eigenschaften HeaderBarHeight und HeaderBarWidth des GridWeb-Steuerelements. Die folgende Abbildung zeigt die Ausgabe des folgenden Codebeispiels.

**Breite und Höhe der Kopfleiste geändert**

![todo: Bild_alt_Text](working-with-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangingWidthandHeightofHeaderBar-ChangingWidthandHeightofHeaderBar.jsp" >}}

## **Arbeiten mit Aspose.Cells.GridWeb Events**

Alle Entwickler müssen mit Ereignissen und ihrem Zweck vertraut sein. Ereignisse werden verwendet, um Benachrichtigungen über Änderungen zu senden, die in einem Steuerelement oder einer Klasse auftreten können. Aspose.Cells. GridWeb verfügt über mehrere Ereignisse, die verwendet werden können, um bestimmte Aufgaben auszuführen, wenn bestimmte Änderungen im Steuerelement auftreten.

Dieses Thema bietet eine Einführung in alle Ereignisse, die vom Aspose.Cells.GridWeb-Steuerelement unterstützt werden, zusammen mit einigen Details zur Behandlung dieser Ereignisse.

### **Einführung in Grid-Events**

Aspose.Cells. Das GridWeb-Steuerelement unterstützt mehrere Ereignisse, die mehr Kontrolle für die Ausführung von Vorgängen bieten, wenn bestimmte Ereignisse im Steuerelement ausgelöst werden. Eine vollständige Liste der vom Aspose.Cells.GridWeb-Steuerelement unterstützten Ereignisse finden Sie unten.

|**Veranstaltungen**|**Beschreibung**|
|:- |:- |
|CellCommand|Tritt auf, wenn auf den Befehls-Hyperlink einer Zelle geklickt wird. Wenn dieses Ereignis ausgelöst wird, stellt sein Parameter e.Argument den Namen des Befehls bereit.|
|CellDoubleClick|Tritt auf, wenn auf die Zelle doppelgeklickt wird.|
|SpalteGelöscht|Tritt auf, wenn ein Benutzer mithilfe des clientseitigen Menüs eine Spalte aus einem Arbeitsblatt löscht.|
|SpalteLöschen|Tritt auf, wenn ein Benutzer versucht, eine Spalte aus einem Arbeitsblatt mithilfe des clientseitigen Menüs zu löschen.|
|ColumnDoubleClick|Tritt auf, wenn auf die Spaltenüberschrift doppelgeklickt wird.|
|Spalte eingefügt|Tritt auf, wenn ein Benutzer über das clientseitige Menü eine Spalte in ein Arbeitsblatt einfügt.|
|CustomCommand|Tritt auf, wenn ein Benutzer auf eine benutzerdefinierte Befehlsschaltfläche klickt.|
|Benutzerdefinierte Daten laden|Tritt auf, wenn die EnableSession-Eigenschaft des Steuerelements auf „false“ festgelegt ist und Arbeitsblattdaten geladen werden müssen. Sie können dieses Ereignis im sitzungslosen Modus behandeln, um Arbeitsblattdaten aus einer Datei oder Datenbank zu laden.|
|SeitenindexGeändert|Tritt auf, wenn der Blattseitenindex des Steuerelements geändert wird.|
|ZeileGelöscht|Tritt auf, wenn ein Benutzer mithilfe des clientseitigen Menüs eine Zeile aus dem Arbeitsblatt löscht.|
|ZeilenLöschen|Tritt auf, wenn ein Benutzer versucht, eine Zeile aus einem Arbeitsblatt mithilfe des clientseitigen Menüs zu löschen.|
|RowDoubleClick|Tritt auf, wenn auf den Zeilenkopf doppelgeklickt wird.|
|Zeile eingefügt|Tritt auf, wenn ein Benutzer über das clientseitige Menü eine Zeile in das Arbeitsblatt einfügt.|
|SaveCommand| Tritt auf, wenn die**Speichern** Schaltfläche angeklickt wird.|
|SheetTabClick|Tritt auf, wenn auf eine Blattregisterkarte geklickt wird.|
|SubmitCommand| Tritt auf, wenn die**Einreichen** Schaltfläche angeklickt wird.|
|Rückgängig-Befehl| Tritt auf, wenn die**Rückgängig machen** Schaltfläche angeklickt wird.|
|AjaxCallFertig|Wird ausgelöst, wenn das AJAX-Update des Steuerelements abgeschlossen ist. (EnableAJAX muss auf true gesetzt werden).|
|CellModifiedOnAjax|Wird ausgelöst, wenn die Zelle im AJAX-Aufruf geändert wird.|
|AfterColumnFilter|Wird ausgelöst, wenn der Filter auf eine Spalte angewendet wird.|

### **Umgang mit Grid-Ereignissen**

Um eine bestimmte Operation beim Auslösen eines bestimmten Ereignisses auszuführen, müssen wir einen Ereignishandler erstellen. Ein Event-Handler führt die gewünschte Aufgabe aus, wenn ein bestimmtes Ereignis ausgelöst wird. Das folgende Beispiel zeigt, wie ein einfaches Grid-Ereignis behandelt wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HandlingGridEvents-HandlingGridEvents.jsp" >}}

## **Arbeiten mit Doppelklick-Ereignissen**

Aspose.Cells.GridWeb enthält drei Arten von Doppelklickereignissen:

- CellDoubleClick, wird ausgelöst, wenn auf eine Zelle doppelgeklickt wird.
- ColumnDoubleClick, wird ausgelöst, wenn auf eine Spaltenüberschrift doppelgeklickt wird.
- RowDoubleClick, wird ausgelöst, wenn auf eine Zeilenüberschrift doppelgeklickt wird.

In diesem Thema wird erläutert, wie Doppelklickereignisse in Aspose.Cells.GridWeb aktiviert werden. Außerdem wird das Erstellen von Ereignishandlern für diese Ereignisse erläutert.

### **Aktivieren von Doppelklickereignissen**

Alle Arten von Doppelklickereignissen können clientseitig aktiviert werden, indem die EnableDoubleClickEvent-Eigenschaft des GridWeb-Steuerelements auf „true“ festgelegt wird.

{{% alert color="primary" %}}

Standardmäßig ist die Eigenschaft „EnableDoubleClickEvent“ auf „false“ gesetzt. Das bedeutet, dass Doppelklickereignisse standardmäßig nicht aktiviert sind. Um solche Ereignisse zu implementieren, aktivieren Sie zuerst die Funktion.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-EnablingDoubleClickEvents-EnablingDoubleClickEvents.jsp" >}}

Sobald Doppelklick-Ereignisse aktiviert sind, ist es möglich, Ereignishandler für beliebige Doppelklick-Ereignisse zu erstellen. Diese Ereignishandler führen bestimmte Aufgaben aus, wenn ein bestimmtes Doppelklickereignis ausgelöst wird.

### **Umgang mit Doppelklickereignissen**

#### **Doppelklicken Sie auf Cell**

Der Ereignishandler für das CellDoubleClick-Ereignis stellt ein Argument vom Typ CellEventArgs bereit, das die vollständigen Informationen der Zelle bereitstellt, auf die doppelgeklickt wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickCell-DoubleClickCell.jsp" >}}

#### **Doppelklicken Sie auf die Spaltenüberschrift**

Der Ereignishandler für das ColumnDoubleClick-Ereignis stellt ein Argument des RowColumnEventArgs-Typs bereit, das die Indexnummer der Spalte für die Überschrift bereitstellt, auf die doppelt geklickt wurde, sowie weitere Informationen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickColumnHeader-DoubleClickColumnHeader.jsp" >}}

#### **Doppelklicken Sie auf den Zeilenkopf**

Der Ereignishandler für das RowDoubleClick-Ereignis stellt ein Argument des RowColumnEventArgs-Typs bereit, das die Indexnummer der Zeile für den Header, auf den doppelgeklickt wurde, und andere zugehörige Informationen bereitstellt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickRowHeader-DoubleClickRowHeader.jsp" >}}

## **Festlegen von Stil oder Aussehen von Aspose.Cells.GridWeb**

Aspose.Cells. GridWeb hat sein eigenes Standard-Look & Feel, aber es ist möglich, sein Aussehen zu ändern. Aspose.Cells.GridWeb bietet mehrere Eigenschaften, mit denen Entwickler das Erscheinungsbild vollständig steuern können. In diesem Thema werden einige dieser Eigenschaften erläutert.

### **Festlegen von Stil oder Aussehen von Aspose.Cells.GridWeb**

#### **Voreingestellte Stile**

Um Entwicklern den Aufwand zu ersparen, bietet Aspose.Cells.GridWeb einige voreingestellte Stile. Wählen Sie einfach einen Stil aus der Liste aus, um den Stil anzuwenden.

|**Stile**|**Farbschema**|
|:- |:- |
|Standard|Silber|
|Bunt1|Rose|
|Bunt2|Blau|
|Profi1|Cyan|
|Profi2|Wieder Cyan|
|Traditionell1|Dunkel|
|Traditionell2|Grau|
|Brauch|Angepasst|
Wenn ein bestimmter Stil ausgewählt wird, ändert er das gesamte Erscheinungsbild des GridWeb-Steuerelements. Entwickler können mithilfe des flexiblen API von Aspose.Cells.GridWeb einen voreingestellten Stil auswählen, der zur Laufzeit angewendet werden soll.

Das GridWeb-Steuerelement stellt die PresetStyle-Eigenschaft bereit, der Entwickler jeden gewünschten voreingestellten Stil zuweisen können.

Die Ausgabe des folgenden Code-Snippets ist unten dargestellt.

**GridWeb-Steuerelement mit darauf angewendetem Colorful1-Stil**

![todo: Bild_alt_Text](working-with-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **Kopfleistenstil**

Wenn Sie sich das GridWeb-Steuerelement ansehen, werden Sie zwei Kopfleisten bemerken. Eine für Spalten (also A, B, C, D usw.) und eine für Zeilen (also 1, 2, 3, 4 usw.). Aspose.Cells.GridWeb ermöglicht es Entwicklern, das Erscheinungsbild dieser Kopfleisten zu steuern. Entwickler können den Stil von Kopfleisten zur Laufzeit festlegen.

{{% alert color="primary" %}}

Das GridWeb-Steuerelement stellt die HeaderBarStyle-Eigenschaft bereit, die einen Stil auf beide Kopfleisten des Steuerelements anwendet.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **Registerkartenleistenstil**

Es ist auch möglich, den Stil der Registerkartenleiste festzulegen. Bitte beachten Sie den folgenden Code

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HeaderBarStyle-HeaderBarStyle.jsp" >}}

#### **Style-Datei wird geladen**

Um Stileinstellungen aus einer vorhandenen Stildatei auf das GridWeb-Steuerelement anzuwenden, können Entwickler den Pfad der Stildatei auf die CustomStyleFileName-Eigenschaft des Steuerelements festlegen. Aber vorher muss die PresetStyle-Eigenschaft des Steuerelements auf Custom gesetzt werden. Dies liegt daran, dass diese Stildatei benutzerdefinierte Stilinformationen enthält, die bereits von einem Entwickler definiert wurden.

Bitte sehen Sie sich das folgende Bild an, das GridWeb mit dem darauf angewendeten benutzerdefinierten Stil zeigt.

![todo: Bild_alt_Text](working-with-gridweb_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-CustomStyleSheet-CustomStyleSheet.jsp" >}}

{{% alert color="primary" %}}

WICHTIG: Das Laden der Stildatei in das GridWeb-Steuerelement wirkt sich nicht auf die Formatierungseinstellungen der Zellen des Steuerelements aus.

{{% /alert %}}

#### **Beispiel für eine benutzerdefinierte Stilvorlage**

Hier ist das Beispiel für eine benutzerdefinierte Stilvorlage. Sie können es gemäß Ihren Anforderungen ändern.

{{< highlight "java" >}}

 <aspose.excel.web.viewerStyletemplate runat="server" HeaderBarWidth="30pt" ScrollBarBaseColor="#AFEEEE" SelectCellBgColor="#FFFAF0" ActiveHeaderBgColor="#DAA520" ActiveCellBgColor="#DDDDFF" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LeftBorderStyle-BorderWidth="" FrameTableStyle-LeftBorderStyle-BorderColor="" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-RightBorderStyle-BorderWidth="" FrameTableStyle-RightBorderStyle-BorderColor="" FrameTableStyle-BorderWidth="1px" FrameTableStyle-CellSpacing="0" FrameTableStyle-BorderColor="#C0FFC0" FrameTableStyle-CellPadding="0" FrameTableStyle-TopBorderStyle-BorderWidth="" FrameTableStyle-TopBorderStyle-BorderColor="" FrameTableStyle-BackColor="#FFFFCC" FrameTableStyle-BottomBorderStyle-BorderWidth="" FrameTableStyle-BottomBorderStyle-BorderColor="" HeaderBarStyle-LeftBorderStyle-BorderWidth="" HeaderBarStyle-LeftBorderStyle-BorderColor="" HeaderBarStyle-verticalalign="Middle" HeaderBarStyle-RightBorderStyle-BorderWidth="" HeaderBarStyle-RightBorderStyle-BorderColor="" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-font-size="10pt" HeaderBarStyle-BorderColor="#00C0C0" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-horizontalalign="Center" HeaderBarStyle-ForeColor="Red" HeaderBarStyle-TopBorderStyle-BorderWidth="" HeaderBarStyle-TopBorderStyle-BorderColor="" HeaderBarStyle-BackColor="#D8BFD8" HeaderBarStyle-BottomBorderStyle-BorderWidth="" HeaderBarStyle-BottomBorderStyle-BorderColor="" ViewTableStyle-LeftBorderStyle-BorderWidth="" ViewTableStyle-LeftBorderStyle-BorderColor="" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-RightBorderStyle-BorderWidth="" ViewTableStyle-RightBorderStyle-BorderColor="" ViewTableStyle-BorderWidth="0px" ViewTableStyle-CellSpacing="0" ViewTableStyle-CellPadding="0" ViewTableStyle-TopBorderStyle-BorderWidth="" ViewTableStyle-TopBorderStyle-BorderColor="" ViewTableStyle-BottomBorderStyle-BorderWidth="" ViewTableStyle-BottomBorderStyle-BorderColor="" BottomTableStyle-LeftBorderStyle-BorderWidth="" BottomTableStyle-LeftBorderStyle-BorderColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-RightBorderStyle-BorderWidth="" BottomTableStyle-RightBorderStyle-BorderColor="" BottomTableStyle-Height="32pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-CellSpacing="0" BottomTableStyle-BorderColor="#80FF80" BottomTableStyle-CellPadding="0" BottomTableStyle-ForeColor="#FFE0C0" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="#FF69B4" BottomTableStyle-BottomBorderStyle-BorderWidth="" BottomTableStyle-BottomBorderStyle-BorderColor="" HeaderBarHeight="15pt" ActiveTabStyle-LeftBorderStyle-BorderWidth="" ActiveTabStyle-LeftBorderStyle-BorderColor="" ActiveTabStyle-RightBorderStyle-BorderWidth="" ActiveTabStyle-RightBorderStyle-BorderColor="" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-font-size="10pt" ActiveTabStyle-BorderColor="#00C0C0" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="#FF00FF" ActiveTabStyle-TopBorderStyle-BorderWidth="" ActiveTabStyle-TopBorderStyle-BorderColor="" ActiveTabStyle-BackColor="#80FFFF" ActiveTabStyle-BottomBorderStyle-BorderWidth="" ActiveTabStyle-BottomBorderStyle-BorderColor="" HeaderBarTableStyle-LeftBorderStyle-BorderWidth="" HeaderBarTableStyle-LeftBorderStyle-BorderColor="" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-RightBorderStyle-BorderWidth="" HeaderBarTableStyle-RightBorderStyle-BorderColor="" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-CellSpacing="0" HeaderBarTableStyle-CellPadding="0" HeaderBarTableStyle-TopBorderStyle-BorderWidth="" HeaderBarTableStyle-TopBorderStyle-BorderColor="" HeaderBarTableStyle-BackColor="#C0FFC0" HeaderBarTableStyle-BottomBorderStyle-BorderWidth="" HeaderBarTableStyle-BottomBorderStyle-BorderColor="" DefaultGridLineColor="#228B22" TabStyle-LeftBorderStyle-BorderWidth="" TabStyle-LeftBorderStyle-BorderColor="" TabStyle-RightBorderStyle-BorderWidth="" TabStyle-RightBorderStyle-BorderColor="" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-font-size="8pt" TabStyle-BorderColor="#8080FF" TabStyle-BorderStyle="Groove" TabStyle-ForeColor="#FFFFCC" TabStyle-TopBorderStyle-BorderWidth="" TabStyle-TopBorderStyle-BorderColor="" TabStyle-BackColor="#C0C0FF" TabStyle-BottomBorderStyle-BorderWidth="" TabStyle-BottomBorderStyle-BorderColor="" scrollbararrowColor="#778899"/>

{{< /highlight >}}

## **Erstellen von Steuerelementen in einem Webformular**

In diesem Artikel erfahren Sie, wie Sie eine einfache Webformular-JSP (Java-Serverseite) mit GridWeb-Steuerelement erstellen.

**Schritt 1 – Verzeichnisstruktur erstellen**

 Sie müssen die folgende Verzeichnisstruktur in der erstellen**webapps**Verzeichnis von Tomcat Server

![todo: Bild_alt_Text](working-with-gridweb_7.png)

 Dies sind die Verzeichnisse und Dateien, die Sie erstellen müssen. Bitte lesen Sie die Kommentare und folgen Sie ihnen. Sie können die neuesten Aspose.Cells.GridWeb for Java Release-Archive von erhalten[dieser Link](https://downloads.aspose.com/cells/java).

{{< highlight "java" >}}

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

**Schritt 2 - Hinzufügen von Codes in erstellten Dateien**

Dieser Abschnitt zeigt den Code für verschiedene Dateien, die in der obigen Verzeichnisstruktur erstellt wurden. Bitte holen Sie sich diese Codes und fügen Sie sie Ihren Dateien hinzu, indem Sie sie in Notepad öffnen und kopieren/einfügen.

**Web.xml**

{{< highlight "java" >}}

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

{{< highlight "java" >}}

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

**Schritt 3 – Ausführen Ihrer Beispiel-JSP-Webseite**

Jetzt haben Sie alles getan. Es ist Zeit, die Webseite auszuführen. Bitte starten Sie Ihren Tomcat-Server und fügen Sie dann die folgende URL in den Webbrowser ein.

{{< highlight "java" >}}

 http://localhost:8080/SamplePageGridWebJava/SamplePage.jsp

{{< /highlight >}}

Sie werden so etwas wie den folgenden Screenshot sehen. Herzlichen Glückwunsch, Sie haben das GridWeb-Steuerelement erfolgreich auf Ihrer JSP-Seite verwendet.

![todo: Bild_alt_Text](working-with-gridweb_8.png)

## **GridWeb drucken**

Es gibt Zeiten, in denen Entwickler den GridWeb-Inhalt drucken müssen, der von einer Webseite enthalten ist, ohne eine Microsoft-Excel-Datei zu speichern. Das Aspose.Cells.GridWeb-Steuerelement unterstützt diese Funktion.

### **GridWeb drucken**

Um zu drucken, ohne eine separate Datei zu speichern, rufen Sie die Methode print() der GridWeb-Klasse clientseitig auf, um das Raster zu drucken. Sie können auch ein geeignetes Ereignis auswählen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-PrintingGridWeb-PrintingGridWeb.jsp" >}}

Da Sie es von der Clientseite aufrufen, müssen Sie zuerst die gridweb-Client-ID abrufen. Sie können die Client-ID mit der Methode gridweb.getClientID() abrufen.

### **Clientseitiger Beispielcode**

Bitte beachten Sie den folgenden Link, der die Methode gridweb.print() von der Clientseite aufruft.

**HTML**

{{< highlight "java" >}}

 <a href="#" onclick='<%=gridweb.getClientID()%>.print(); '>Print Function of GridWeb</a>

{{< /highlight >}}

## **Einführung in verschiedene Grid-Modi**

Dieser Artikel beschreibt die verschiedenen Modi von Aspose.Cells.GridWeb. Diese Modi unterscheiden sich logisch aufgrund ihrer unterschiedlichen Merkmale und Verhaltensweisen. Wir haben verschiedene Arten von Modi identifiziert als:

- Bearbeitungsmodus
- Ansichtsmodus

Alle diese Modi haben ihre eigenen Eigenschaften. Entwickler können mit Aspose.Cells.GridWeb in jedem Modus entsprechend ihren Anforderungen arbeiten. Wir werden uns jeden Modus unten ansehen.

### **Bearbeitungsmodus**

Standardmäßig befindet sich das Aspose.Cells.GridWeb-Steuerelement im Bearbeitungsmodus. Im Bearbeitungsmodus können Sie den Rasterinhalt vollständig bearbeiten oder ändern, indem Sie alle Funktionen verwenden, die das Steuerelement Aspose.Cells.GridWeb bietet. Zu diesen Funktionen gehören:

- Speichern des Rasterinhalts in Microsoft Excel-Dateien.
- Senden von Daten an einen Server.
- Formeln berechnen.
- Vorherige Aktionen rückgängig machen oder verwerfen.
- Zeilen und Spalten verwalten.
- Ausschneiden, Kopieren oder Einfügen von Daten.
- Zellen formatieren usw.

**GridWeb-Steuerelement im Bearbeitungsmodus**

![todo: Bild_alt_Text](working-with-gridweb_9.png)

Entwickler können auch programmgesteuert in den Bearbeitungsmodus wechseln, indem sie die EditMode-Eigenschaft des GridWeb-Steuerelements auf true festlegen.

### **Codebeispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebEditMode-GridWebEditMode.jsp" >}}

### **Ansichtsmodus**

Wenn sich das GridWeb-Steuerelement im Ansichtsmodus befindet, können Benutzer den Rasterinhalt nicht bearbeiten oder ändern, was bedeutet, dass Benutzer den Rasterinhalt nur anzeigen können. Deshalb wird dieser Modus Ansichtsmodus genannt. Im Ansichtsmodus sind einige Schaltflächen (**Einreichen**, **Speichern** und**Rückgängig machen** ) sind ausgeblendet und das Menü, das beim Rechtsklick erscheint, enthält nur die**Kopieren** und**Finden** Möglichkeit.

**GridWeb-Steuerelement im Ansichtsmodus** 

![todo: Bild_alt_Text](working-with-gridweb_10.png)

 Wenn Entwickler möchten, dass ihre Benutzer nur Daten anzeigen, können sie programmgesteuert in den Ansichtsmodus wechseln, indem sie die EditMode-Eigenschaft des GridWeb-Steuerelements auf festlegen**FALSCH**.

### **Codebeispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebViewMode-GridWebViewMode.jsp" >}}

{{% alert color="primary" %}}

Auch im Ansichtsmodus können Benutzer die Höhe und Breite von Zeilen und Spalten ändern.

{{% /alert %}}
