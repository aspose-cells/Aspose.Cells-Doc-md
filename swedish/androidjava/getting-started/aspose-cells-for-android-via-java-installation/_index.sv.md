---
title: Aspose.Cells för Android via Java-installation
type: docs
weight: 30
url: /sv/java/aspose-cells-for-android-via-java-installation/
---
## **Systemkrav**
Aspose.Cells för Android via Java är plattformsoberoende och kan användas på alla plattformar där Android Runtime-miljön är installerad och kommer att köras på Android-system som kör Android OS 2.0 eller senare. För närvarande har komponenten testats med:

- Android 5.1 v 22
## **Installera Aspose.Cells för Android via Java från Maven Repository**
1. Lägg till maven repository i din build.gradle
1. Lägg till 'Aspose.Cells för Android via Java' JAR som ett beroende

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
## **Hur man använder Aspose.Cells för Android via Java**
Det här avsnittet guidar dig genom de nödvändiga stegen för att ställa in Aspose.Cells för Android via Java i Android Studio IDE, förutsatt att du redan har den senaste versionen av Android Studio installerad på din maskin och att du även har skaffat den senaste versionen av Aspose.Cells för Android via Java paket.

{{% alert color="primary" %}} 

Om du inte har installerat Android Studio ännu, måste du först skaffa installationen av Android Studio och installera den på din maskin. Du kan ladda ner den senaste versionen av Android Studio från[här](https://developer.android.com/studio/index.html#win-bundle) medan detaljerna om hur man installerar IDE finns tillgängliga[här](https://developer.android.com/studio/install.html).

{{% /alert %}} {{% alert color="primary" %}} 

 Aspose.Cells för Android via Java-paketet kan laddas ner från[här](https://downloads.aspose.com/cells/androidjava). Observera att varje releasepaket med Aspose.Cells för Android via Java huvudsakligen består av 2 filer enligt beskrivningen nedan.

- **aspose-celler-xxxjar** är huvudbiblioteksfilen som innehåller alla namnområden från Aspose.Cells för Android via Java API.
- **aspose-cells-xxx-libs.apk** är APK-filen som innehåller den tredje parten bcprov-jdk15-146.jar som används för kryptering och dekrypteringsmöjligheter som erbjuds av Aspose.Cells för Android via Java API.

{{% /alert %}} 
### **Komma igång med Aspose.Cells för Android via Java i Android Studio**
När Android Studio IDE har laddats, klicka på Arkiv > Nytt > Nytt projekt som visas nedan.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_1.png)

Du kan också skapa ett nytt projekt från Android Studios välkomstskärm som visas nedan.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_2.png)

Därefter kommer du att bli ombedd att ange applikationsnamn, domän och plats för att lagra projektfilerna. Du kan välja att ändra standardvärdena enligt ditt val eller låta dem vara som de är och klicka på Nästa.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_3.png)

I nästa steg måste du ange vilken Android-enhet du vill vara värd för/köra din applikation. När du har valt, klicka på knappen Nästa.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_4.png)

Nu måste du välja aktiviteten från en fördefinierad lista med mallar. För att hålla demonstrationen enkel har vi valt Empty Activity-mallen som visas nedan.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_5.png)

Klicka på knappen Slutför i dialogrutan Anpassa aktiviteten eftersom vi kommer att behålla alla standardinställningar som de är.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_6.png)

Så snart du klickar på knappen Slutför i föregående steg, kommer IDE att börja bygga projektet enligt nedan. Låt det avslutas eller klicka på Avbryt-knappen.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_7.png)

Nu har projektet laddats i IDE, men du kanske vill ändra vyn till Project så att du kan se hela hierarkin av projektfilerna. För att ändra vyn, kontrollera följande ögonblicksbild.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_8.png)

 Efter att ha ändrat vyn till Project, hitta och ladda**bygga.gradle** fil i editorn och klistra in följande utdrag som visas nedan.

{{< highlight "java" >}}

 dexOptions{

    javaMaxHeapSize "4g"

}

{{< /highlight >}}

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_9.png)

Därefter kommer vi att lägga till Aspose.Cells för Android via Java Jar till projektet. Det finns två viktiga steg som beskrivs nedan.

-  Kopiera manuellt Aspose.Cells för Android via Java Jar till**\app\libs** mapp.
- Lägg till Aspose.Cells för Android via Java Jar som bibliotek till modulen som visas nedan.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_10.png)

Du kommer att bli ombedd att välja den modul till vilken du vill lägga till Aspose.Cells för Java.Android Jar som ett bibliotek. Välj lämpligt och klicka på OK.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_11.png)

 Du måste också lägga till APK-filen till projektet. Du måste kopiera APK-filen till**\app\src\main\tillgångar**mapp. Om du inte har tillgångsmappen under huvudmappen kan du skapa en genom att högerklicka på huvudnoden i projektvyn. Välj Ny > Mapp > Tillgångsmapp.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_12.png)

När APK-filen har lagts till i projektet måste den laddas av projektet. Det finns två sätt att ladda APK:n enligt följande.

- Ladda APK:en i en anpassad applikationsklass med hjälp av kodavsnittet nedan och registrera den anpassade applikationsklassen till AndroidManifest.xml.

{{< highlight "java" >}}

 LibsLoadHelper.loadLibs(this);

{{< /highlight >}}

- Ladda APK-filen i OnCreate-metoden för MainActivity.

{{< highlight "java" >}}

 LibsLoadHelper.loadLibs(getApplicationContext());

{{< /highlight >}}

Nu är vi redo att skriva koden. För att hålla demonstrationen lätt att förstå har vi lagt till en knappwidget i layouten och kommer att hantera dess klickhändelse enligt följande.

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

När du kör programmet med hjälp av play-knappen på IDE-gränssnittet (eller använder SHIFT + F10) kommer emulatorn att ladda programmet enligt nedan.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_13.png)

Genom att klicka på knappen på emulatorn körs koden för att skapa ett nytt kalkylblad i emulatorns externa lagringsmapp. Du kan komma åt filen från Android Device Monitor som visas nedan.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_14.png)

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_15.png)


