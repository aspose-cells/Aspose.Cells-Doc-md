---
title: Aspose.Cells für Android via Java Installation
type: docs
weight: 30
url: /de/java/aspose-cells-for-android-via-java-installation/
---

## **Systemanforderungen**
Aspose.Cells für Android via Java ist plattformunabhängig und kann auf jeder Plattform verwendet werden, auf der die Android-Laufzeitumgebung installiert ist und auf Android-Systemen mit Android OS 2.0 oder höher ausgeführt wird. Derzeit wurde das Komponente mit folgendem getestet:

- Android 5.1 v 22
## **Installieren Sie Aspose.Cells für Android via Java aus dem Maven-Repository**
1. Fügen Sie das Maven-Repository in Ihre build.gradle-Datei ein 
1. Fügen Sie 'Aspose.Cells für Android via Java' JAR als Abhängigkeit hinzu

{{< highlight java >}}

 // 1. Add maven repository into your build.gradle 

repositories {

    mavenCentral()

    maven { url "http://repository.aspose.com/repo/" }

}

// 2. Add 'Aspose.Cells for Android via Java' JAR as a dependency

dependencies {

    ...

    ...

    compile (group: 'com.aspose', name: 'aspose-cells', version: '25.9', classifier: 'android.via.java')

}

{{< /highlight >}}
## **Verwendung von Aspose.Cells für Android via Java**
Dieses Thema führt Sie durch die notwendigen Schritte zur Einrichtung von Aspose.Cells für Android via Java in der Android Studio-IDE, vorausgesetzt, dass Sie bereits die neueste Version von Android Studio auf Ihrem Rechner installiert haben und auch die neueste Version des Aspose.Cells für Android via Java-Pakets erworben haben.

{{% alert color="primary" %}} 

Wenn Sie das Android Studio noch nicht installiert haben, müssen Sie zuerst das Setup von Android Studio erwerben und auf Ihrem Rechner installieren. Sie können die neueste Version von Android Studio von [hier](https://developer.android.com/studio/index.html#win-bundle) herunterladen, während die Details zur Installation der IDE [hier](https://developer.android.com/studio/install.html) verfügbar sind.

{{% /alert %}} {{% alert color="primary" %}} 

Das Aspose.Cells für Android via Java-Paket kann von [hier](https://downloads.aspose.com/cells/androidjava) heruntergeladen werden. Bitte beachten Sie, dass jedes Veröffentlichungspaket von Aspose.Cells für Android via Java hauptsächlich aus 2 Dateien besteht, wie unten detailliert.

- **aspose-cells-x.x.x.jar** ist die Hauptbibliotheksdatei, die alle Namespaces der Aspose.Cells für Android via Java-API enthält.
- **aspose-cells-x.x.x-libs.apk** ist die APK, die die 3rd-Party-Datei bcprov-jdk15-146.jar enthält, die für die Verschlüsselungs- und Entschlüsselungsfunktionen der Aspose.Cells für Android via Java-API verwendet wird.

{{% /alert %}} 
### **Erste Schritte mit Aspose.Cells für Android via Java in Android Studio**
Sobald die Android Studio IDE geladen ist, klicken Sie auf Datei > Neu > Neues Projekt, wie unten gezeigt.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_1.png)

Sie können auch ein neues Projekt von dem Begrüßungsbildschirm von Android Studio aus erstellen, wie unten gezeigt.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_2.png)

Als nächstes werden Sie aufgefordert, den Anwendungsnamen, den Domainnamen und den Speicherort für die Projektdateien anzugeben. Sie können wählen, die Standardwerte nach Ihrem Wunsch zu ändern oder sie so zu belassen, wie sie sind, und auf Weiter klicken.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_3.png)

Im nächsten Schritt müssen Sie das Android-Gerät auswählen, auf dem Sie Ihre Anwendung hosten/ausführen möchten. Nach der Auswahl klicken Sie auf die Schaltfläche Weiter.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_4.png)

Sie müssen nun die Aktivität aus einer vordefinierten Liste von Vorlagen auswählen. Um die Demonstration einfach zu halten, haben wir die Vorlage für eine Leere Aktivität ausgewählt, wie unten gezeigt.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_5.png)

Klicken Sie auf die Schaltfläche Fertig stellen im Dialogfeld zur Anpassung der Aktivität, da wir alle Standardeinstellungen beibehalten werden.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_6.png)

Sobald Sie auf die Schaltfläche Fertig stellen im vorherigen Schritt klicken, beginnt die IDE mit dem Aufbau des Projekts, wie unten gezeigt. Lassen Sie es fertig stellen oder klicken Sie auf die Schaltfläche Abbrechen.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_7.png)

Das Projekt wurde nun in der IDE geladen, jedoch möchten Sie möglicherweise die Ansicht auf Projekt ändern, um die vollständige Hierarchie der Projektdateien anzuzeigen. Um die Ansicht zu ändern, überprüfen Sie bitte den folgenden Schnappschuss.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_8.png)

Nachdem Sie die Ansicht auf Projekt geändert haben, finden Sie die **build.gradle**-Datei im Editor und fügen Sie das folgende Snippet wie unten gezeigt ein.

{{< highlight java >}}

 dexOptions{

    javaMaxHeapSize "4g"

}

{{< /highlight >}}

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_9.png)

Als nächstes fügen wir das Aspose.Cells for Android via Java Jar dem Projekt hinzu. Es gibt 2 wichtige Schritte, wie unten beschrieben.

- Kopieren Sie manuell das Aspose.Cells for Android via Java-Jar in den **\app\libs**-Ordner.
- Fügen Sie das Aspose.Cells for Android via Java Jar als Bibliothek zum Modul hinzu, wie unten gezeigt.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_10.png)

Sie werden aufgefordert, das Modul auszuwählen, zu dem Sie das Aspose.Cells for Java.Android Jar als Bibliothek hinzufügen möchten. Bitte wählen Sie entsprechend aus und klicken Sie auf OK.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_11.png)

Sie müssen auch die APK-Datei zum Projekt hinzufügen. Sie müssen die APK in den **\app\src\main\assets**-Ordner kopieren. Wenn Sie den assets-Ordner unter dem main-Ordner nicht haben, können Sie einen erstellen, indem Sie mit der rechten Maustaste auf den Hauptknoten in der Projektansicht klicken. Wählen Sie Neu > Ordner > Asset-Ordner.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_12.png)

Sobald die APK dem Projekt hinzugefügt wurde, muss sie vom Projekt geladen werden. Es gibt 2 Möglichkeiten, die APK wie folgt zu laden.

- Laden Sie die APK in einer benutzerdefinierten Anwendungsklasse mithilfe des unten bereitgestellten Snippets und registrieren Sie die benutzerdefinierte Anwendungsklasse in der AndroidManifest.xml.

{{< highlight java >}}

 LibsLoadHelper.loadLibs(this);

{{< /highlight >}}

- Laden Sie die APK in der OnCreate-Methode der MainActivity.

{{< highlight java >}}

 LibsLoadHelper.loadLibs(getApplicationContext());

{{< /highlight >}}

Nun sind wir bereit, den Code zu schreiben. Um die Demonstration einfach zu verstehen, haben wir ein Schaltflächen-Widget zum Layout hinzugefügt und werden dessen Klickereignis behandeln, wie unten beschrieben.

{{< highlight java >}}

 private class TestTask extends AsyncTask<Void, String, Boolean> {

    @Override

    protected Boolean doInBackground(Void... params) {

        Boolean result = false;

        Workbook book = new Workbook();

        Worksheet sheet = book.getWorksheets().get(0);

        Cells cells = sheet.getCells();

        Cell cell = cells.get("A1");

        cell.putValue("Hello World!");

        try {

            book.save(SD_PATH + "output.xlsx");

        } catch (Exception e) {

            e.printStackTrace();

        }

        return result;

    }

}

{{< /highlight >}}

Wenn Sie die Anwendung mithilfe der Wiedergabeschaltfläche in der IDE-Benutzeroberfläche starten (oder mit SHIFT + F10), lädt der Emulator die Anwendung, wie unten gezeigt.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_13.png)

Durch Klicken der Schaltfläche auf dem Emulator wird der Code ausgeführt, um eine neue Arbeitsmappe im externen Speicherordner des Emulators zu erstellen. Sie können auf die Datei vom Android Device Monitor aus zugreifen, wie unten gezeigt.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_14.png)

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_15.png)


