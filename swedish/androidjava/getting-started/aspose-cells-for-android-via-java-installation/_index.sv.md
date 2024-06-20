---
title: Installera Aspose.Cells för Android via Java
type: docs
weight: 30
url: /sv/java/aspose-cells-for-android-via-java-installation/
---

## **Systemkrav**
Aspose.Cells for Android via Java är plattformsoberoende och kan användas på vilken plattform som helst där Android Runtime-miljön är installerad och kommer att köras på Android-system som kör Android OS 2.0 eller högre. För närvarande har komponenten testats med:

- Android 5.1 v 22
## **Installera Aspose.Cells för Android via Java från Maven Repository**
1. Lägg till maven-repository i din build.gradle 
1. Lägg till 'Aspose.Cells for Android via Java' JAR som en beroende

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

    compile (group: 'com.aspose', name: 'aspose-cells', version: '20.6', classifier: 'android.via.java')

}

{{< /highlight >}}
## **Hur man använder Aspose.Cells for Android via Java**
Detta ämne kommer att guida dig genom de nödvändiga stegen för att konfigurera Aspose.Cells for Android via Java i Android Studio IDE, förutsatt att du redan har den senaste versionen av Android Studio installerad på din dator och har även förvärvat den senaste versionen av Aspose.Cells for Android via Java-paketet.

{{% alert color="primary" %}} 

Om du inte har installerat Android Studio ännu måste du först skaffa setupen för Android Studio och installera den på din dator. Du kan ladda ner den senaste versionen av Android Studio från [här](https://developer.android.com/studio/index.html#win-bundle) medan information om hur man installerar IDE finns tillgänglig [här](https://developer.android.com/studio/install.html).

{{% /alert %}} {{% alert color="primary" %}} 

Paketet Aspose.Cells for Android via Java kan laddas ner från [här](https://downloads.aspose.com/cells/androidjava). Observera, varje releasepaket av Aspose.Cells for Android via Java består främst av 2 filer enligt nedan:

- **aspose-cells-x.x.x.jar** är huvudbiblioteksfilen som innehåller alla namespaces från Aspose.Cells for Android via Java API.
- **aspose-cells-x.x.x-libs.apk** är APK-filen som innehåller den tredjeparts bcprov-jdk15-146.jar som används för krypterings- och dekrypteringsfunktionerna som erbjuds av Aspose.Cells för Android via Java API.

{{% /alert %}} 
### **Komma igång med Aspose.Cells för Android via Java i Android Studio**
När Android Studio IDE har laddats, klicka på Fil > Ny > Nytt projekt som visas nedan.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_1.png)

Du kan också skapa ett nytt projekt från välkomstskärmen i Android Studio som visas nedan.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_2.png)

Nästa steg är att ange applikationsnamn, domän och plats för att lagra projektfilerna. Du kan välja att ändra standardvärdena enligt ditt val eller låta dem vara som de är och klicka på Nästa.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_3.png)

I nästa steg måste du ange vilken Android-enhet du vill vara värd/köra din applikation på. När du har valt, klicka på Nästa-knappen.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_4.png)

Nu måste du välja aktivitet från en fördefinierad lista med mallar. För att hålla demonstrationen enkel har vi valt mallen Tom aktivitet som visas nedan.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_5.png)

Klicka på Avsluta-knappen på anpassningsdialogrutan för aktiviteten eftersom vi kommer att behålla alla standardinställningarna som de är.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_6.png)

Så snart du har klickat på Avsluta-knappen i det föregående steget kommer IDE att börja bygga projektet som visas nedan. Låt det slutföras eller klicka på Avbryt-knappen.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_7.png)

Nu har projektet laddats in i IDE:n, men du kanske vill ändra vyn till Projekt så att du kan se hela hierarkin av projektfilerna. För att ändra vyn, se följande ögonblicksbild.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_8.png)

Efter att ha ändrat vyn till Projekt, hitta och ladda in filen **build.gradle** i redigeraren och klistra in följande utdrag som visas nedan.

{{< highlight java >}}

 dexOptions{

    javaMaxHeapSize "4g"

}

{{< /highlight >}}

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_9.png)

Nästa steg är att lägga till Aspose.Cells för Android via Java Jar till projektet. Det finns 2 viktiga steg enligt nedan.

- Kopiera manuellt Aspose.Cells för Android via Java Jar till mappen **\app\libs**.
- Lägg till Aspose.Cells för Android via Java Jar som ett bibliotek till modulen enligt nedan.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_10.png)

Du kommer att bli ombedd att välja modulen till vilken du vill lägga till Aspose.Cells for Java.Android Jar som ett bibliotek. Välj lämpligt och klicka på OK.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_11.png)

Du måste också lägga till APK-filen i projektet. Du måste kopiera APK till mappen **\app\src\main\assets**. Om du inte har mappen assets under huvudmappen kan du skapa en genom att högerklicka på huvudnoden i Projektvyn. Välj Nytt > Mapp > Tillgångsmapp.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_12.png)

När APK-filen har lagts till i projektet måste den laddas av projektet. Det finns 2 sätt att ladda APK:n på som följer.

- Ladda in APK:n i en anpassad applikationsklass med hjälp av det angivna utdraget nedan och registrera den anpassade applikationsklassen i AndroidManifest.xml.

{{< highlight java >}}

 LibsLoadHelper.loadLibs(this);

{{< /highlight >}}

- Ladda in APK:n i metoden OnCreate i MainActivity.

{{< highlight java >}}

 LibsLoadHelper.loadLibs(getApplicationContext());

{{< /highlight >}}

Nu är vi redo att skriva koden. För att hålla demonstrationen lätt att förstå har vi lagt till en knapp-widget i layouten och kommer att hantera dess klickhändelse enligt nedan.

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

När du kör applikationen med hjälp av playknappen på IDE-gränssnittet (eller med SHIFT + F10) kommer emulatorn att ladda in applikationen som visas nedan.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_13.png)

Genom att klicka på knappen på emulatorn kommer koden att köras för att skapa ett nytt kalkylblad i den externa lagringsmappen för emulatorn. Du kan komma åt filen från Android Device Monitor som visas nedan.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_14.png)

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_15.png)


