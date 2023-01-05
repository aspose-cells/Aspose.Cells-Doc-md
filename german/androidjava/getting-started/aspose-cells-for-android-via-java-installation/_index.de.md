---
title: Aspose.Cells for Android via Java Installation
type: docs
weight: 30
url: /de/java/aspose-cells-for-android-via-java-installation/
---
## **System Anforderungen**
Aspose.Cells for Android via Java ist plattformunabhängig und kann auf jeder Plattform verwendet werden, auf der die Android-Laufzeitumgebung installiert ist, und läuft auf Android-Systemen mit Android OS 2.0 oder höher. Derzeit wurde das Bauteil getestet mit:

- Android 5.1 Version 22
## **Installieren Sie Aspose.Cells for Android via Java aus dem Maven-Repository**
1. Fügen Sie das Repository maven zu Ihrem Build hinzu.gradle
1. Fügen Sie 'Aspose.Cells for Android via Java' JAR als Abhängigkeit hinzu

{{< highlight "java" >}}

 // 1. Add maven repository into your build.gradle 

repositories {

    mavenCentral()

    maven { url "http://repository.aspose.com/repo/" }

}

// 2. Add 'Aspose.Cells for Android via Java' JAR as a dependency

dependencies {

    ...

    ...

    compile (group: 'com.aspose', name: 'aspose-cells', version: '20.6', classifier: 'android.via.java')

}

{{< /highlight >}}
## **So verwenden Sie Aspose.Cells for Android via Java**
Dieses Thema führt Sie durch die erforderlichen Schritte zum Einrichten von Aspose.Cells for Android via Java in Android Studio IDE, vorausgesetzt, Sie haben bereits die neueste Version von Android Studio auf Ihrem Computer installiert und Sie haben auch die neueste Version des Pakets Aspose.Cells for Android via Java erworben.

{{% alert color="primary" %}} 

Wenn Sie Android Studio noch nicht installiert haben, müssen Sie zuerst das Setup von Android Studio erwerben und auf Ihrem Computer installieren. Sie können die neueste Version von Android Studio von herunterladen[Hier](https://developer.android.com/studio/index.html#win-bundle) während die Details zur Installation der IDE verfügbar sind[Hier](https://developer.android.com/studio/install.html).

{{% /alert %}} {{% alert color="primary" %}} 

 Aspose.Cells for Android via Java Paket kann heruntergeladen werden[Hier](https://downloads.aspose.com/cells/androidjava). Bitte beachten Sie, dass jedes Release-Paket von Aspose.Cells for Android via Java hauptsächlich aus 2 Dateien besteht, wie unten beschrieben.

- **aspose-cells-xxxjar** ist die Hauptbibliotheksdatei, die alle Namespaces von Aspose.Cells for Android via Java API enthält.
- **aspose-cells-xxx-libs.apk** ist das APK, das die Drittanbieterdatei bcprov-jdk15-146.jar enthält, die für Verschlüsselungs- und Entschlüsselungsfunktionen verwendet wird, die von Aspose.Cells for Android via Java API angeboten werden.

{{% /alert %}} 
### **Erste Schritte mit Aspose.Cells for Android via Java in Android Studio**
Sobald die Android Studio IDE geladen ist, klicken Sie wie unten gezeigt auf Datei > Neu > Neues Projekt.

![todo: Bild_alt_Text](aspose-cells-for-android-via-java-installation_1.png)

Sie können auch ein neues Projekt über den Begrüßungsbildschirm von Android Studio erstellen, wie unten gezeigt.

![todo: Bild_alt_Text](aspose-cells-for-android-via-java-installation_2.png)

Als Nächstes werden Sie aufgefordert, den Anwendungsnamen, die Domäne und den Speicherort zum Speichern der Projektdateien anzugeben. Sie können die Standardwerte nach Ihrer Wahl ändern oder sie unverändert lassen und auf Weiter klicken.

![todo: Bild_alt_Text](aspose-cells-for-android-via-java-installation_3.png)

Im nächsten Schritt müssen Sie das Android-Gerät angeben, auf dem Sie Ihre Anwendung hosten/ausführen möchten. Klicken Sie nach der Auswahl auf die Schaltfläche Weiter.

![todo: Bild_alt_Text](aspose-cells-for-android-via-java-installation_4.png)

Jetzt müssen Sie die Aktivität aus einer vordefinierten Liste von Vorlagen auswählen. Um die Demonstration einfach zu halten, haben wir die Vorlage „Leere Aktivität“ ausgewählt, wie unten gezeigt.

![todo: Bild_alt_Text](aspose-cells-for-android-via-java-installation_5.png)

Klicken Sie im Dialogfeld "Aktivität anpassen" auf die Schaltfläche "Fertig stellen", da alle Standardeinstellungen unverändert bleiben.

![todo: Bild_alt_Text](aspose-cells-for-android-via-java-installation_6.png)

Sobald Sie im vorherigen Schritt auf die Schaltfläche „Fertig stellen“ geklickt haben, beginnt die IDE mit dem Erstellen des Projekts, wie unten gezeigt. Lassen Sie es fertig oder klicken Sie auf die Schaltfläche Abbrechen.

![todo: Bild_alt_Text](aspose-cells-for-android-via-java-installation_7.png)

Jetzt wurde das Projekt in die IDE geladen, aber vielleicht möchten Sie die Ansicht auf Projekt ändern, damit Sie die vollständige Hierarchie der Projektdateien sehen können. Um die Ansicht zu ändern, überprüfen Sie bitte den folgenden Schnappschuss.

![todo: Bild_alt_Text](aspose-cells-for-android-via-java-installation_8.png)

 Nachdem Sie die Ansicht auf Projekt geändert haben, suchen und laden Sie die**bau.gradle** Datei im Editor und fügen Sie das folgende Snippet wie unten gezeigt ein.

{{< highlight "java" >}}

 dexOptions{

    javaMaxHeapSize "4g"

}

{{< /highlight >}}

![todo: Bild_alt_Text](aspose-cells-for-android-via-java-installation_9.png)

Als Nächstes fügen wir dem Projekt das Glas Aspose.Cells for Android via Java hinzu. Es gibt 2 wichtige Schritte, wie unten beschrieben.

-  Kopieren Sie das Glas Aspose.Cells for Android via Java manuell in die**\app\libs** Mappe.
- Fügen Sie Aspose.Cells for Android via Java Jar als Bibliothek zum Modul hinzu, wie unten gezeigt.

![todo: Bild_alt_Text](aspose-cells-for-android-via-java-installation_10.png)

Sie werden aufgefordert, das Modul auszuwählen, dem Sie das Aspose.Cells for Java.Android Jar als Bibliothek hinzufügen möchten. Bitte treffen Sie eine entsprechende Auswahl und klicken Sie auf OK.

![todo: Bild_alt_Text](aspose-cells-for-android-via-java-installation_11.png)

 Sie müssen auch die APK-Datei zum Projekt hinzufügen. Du musst die APK in die kopieren**\app\src\main\assets**Mappe. Wenn Sie den Assets-Ordner nicht unter dem Hauptordner haben, können Sie einen erstellen, indem Sie mit der rechten Maustaste auf den Hauptknoten in der Projektansicht klicken. Wählen Sie Neu > Ordner > Asset-Ordner.

![todo: Bild_alt_Text](aspose-cells-for-android-via-java-installation_12.png)

Nachdem das APK zum Projekt hinzugefügt wurde, muss es vom Projekt geladen werden. Es gibt zwei Möglichkeiten, die APK wie folgt zu laden.

- Laden Sie das APK mithilfe des unten bereitgestellten Snippets in eine benutzerdefinierte Anwendungsklasse und registrieren Sie die benutzerdefinierte Anwendungsklasse in AndroidManifest.xml.

{{< highlight "java" >}}

 LibsLoadHelper.loadLibs(this);

{{< /highlight >}}

- Laden Sie das APK in die OnCreate-Methode von MainActivity.

{{< highlight "java" >}}

 LibsLoadHelper.loadLibs(getApplicationContext());

{{< /highlight >}}

Jetzt können wir den Code schreiben. Um die Demonstration leicht verständlich zu halten, haben wir dem Layout ein Schaltflächen-Widget hinzugefügt und behandeln dessen Klick-Ereignis wie folgt.

{{< highlight "java" >}}

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

Wenn Sie die Anwendung mit der Play-Schaltfläche auf der IDE-Oberfläche (oder mit SHIFT + F10) ausführen, lädt der Emulator die Anwendung wie unten gezeigt.

![todo: Bild_alt_Text](aspose-cells-for-android-via-java-installation_13.png)

Durch Klicken auf die Schaltfläche im Emulator wird der Code ausgeführt, um eine neue Tabelle im externen Speicherordner des Emulators zu erstellen. Sie können wie unten gezeigt über den Android Device Monitor auf die Datei zugreifen.

![todo: Bild_alt_Text](aspose-cells-for-android-via-java-installation_14.png)

![todo: Bild_alt_Text](aspose-cells-for-android-via-java-installation_15.png)


