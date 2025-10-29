---
title: Установка Aspose.Cells для Android via Java
type: docs
weight: 30
url: /ru/java/aspose-cells-for-android-via-java-installation/
---

## **Системные требования**
Aspose.Cells для Android via Java  является платформенно-независимой и может использоваться на любой платформе, где установлена среда выполнения Android, и будет работать на системах Android с Android OS 2.0 и выше. В настоящее время компонент протестирован с:

- Android 5.1 v 22
## **Установка Aspose.Cells для Android via Java из репозитория Maven**
1. Добавьте репозиторий Maven в ваш build.gradle 
1. Добавьте 'Aspose.Cells для Android via Java' JAR в качестве зависимости

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
## **Как использовать Aspose.Cells для Android via Java**
В этой теме будет показано, как настроить Aspose.Cells для Android via Java в среде разработки Android Studio, предполагая, что у вас уже установлена последняя версия Android Studio, и вы также получили последнюю версию пакета Aspose.Cells для Android via Java.

{{% alert color="primary" %}} 

Если вы еще не установили Android Studio, вам сначала нужно получить установочный файл Android Studio и установить его на своем компьютере. Вы можете загрузить последнюю версию Android Studio [отсюда](https://developer.android.com/studio/index.html#win-bundle), а подробности о том, как установить IDE, доступны [здесь](https://developer.android.com/studio/install.html).

{{% /alert %}} {{% alert color="primary" %}} 

Пакет Aspose.Cells для Android via Java можно загрузить [здесь](https://downloads.aspose.com/cells/androidjava). Обратите внимание, что каждый пакет выпуска Aspose.Cells для Android via Java в основном состоит из 2 файлов, подробно описанных ниже.

- **aspose-cells-x.x.x.jar** - это основной файл библиотеки, содержащий все пространства имен из API Aspose.Cells для Android via Java.
- **aspose-cells-x.x.x-libs.apk** - это APK, содержащий сторонний bcprov-jdk15-146.jar, используемый для функций шифрования и дешифрования, предлагаемых API Aspose.Cells для Android via Java.

{{% /alert %}} 
### **Начало работы с Aspose.Cells для Android via Java в Android Studio**
Как только загружается среда разработки Android Studio, щелкните Файл > Новый > Новый проект, как показано ниже.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_1.png)

Вы также можете создать новый проект со страницы приветствия Android Studio, как показано ниже.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_2.png)

Затем вас попросят указать название приложения, домен и место для хранения файлов проекта. Вы можете выбрать изменить значения по умолчанию по вашему усмотрению или оставить их такими, какие они есть, и нажать Далее.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_3.png)

На следующем этапе вам нужно будет указать устройство Android, на котором вы хотите запустить ваше приложение. После выбора нажмите кнопку Далее.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_4.png)

Теперь вам нужно выбрать Activity из предопределенного списка шаблонов. Чтобы упростить демонстрацию, мы выбрали шаблон Пустая Activity, как показано ниже.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_5.png)

Щелкните кнопку Завершить на диалоговом окне Настройка Activity, поскольку мы оставим все значения по умолчанию.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_6.png)

Как только вы щелкнете кнопку Завершить на предыдущем этапе, среда разработки начнет сборку проекта, как показано ниже. Дайте ей завершиться или нажмите кнопку Отмена.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_7.png)

Теперь проект загружен в среде разработки, однако вы можете захотеть изменить вид на Проект, чтобы видеть полную иерархию файлов проекта. Чтобы изменить вид, проверьте следующий снимок экрана.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_8.png)

После изменения вида на Проект найдите и откройте файл **build.gradle** в редакторе и вставьте следующий фрагмент, как показано ниже.

{{< highlight java >}}

 dexOptions{

    javaMaxHeapSize "4g"

}

{{< /highlight >}}

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_9.png)

Затем мы добавим Jar Aspose.Cells для Android via Java в проект. Есть 2 важных шага, подробно описанных ниже.

- Вручную скопируйте Jar Aspose.Cells для Android via Java в папку **\app\libs**.
- Добавьте Jar Aspose.Cells для Android via Java как библиотеку в модуль, как показано ниже.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_10.png)

Вас попросят выбрать модуль, в который вы хотите добавить Aspose.Cells for Java.Android Jar в качестве библиотеки. Пожалуйста, сделайте соответствующий выбор и нажмите OK.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_11.png)

Вам также нужно добавить файл APK в проект. Вам нужно скопировать APK в папку **\app\src\main\assets**. Если у вас нет папки assets внутри папки main, вы можете создать ее, щелкнув правой кнопкой мыши на узле main в виде проекта. Выберите New > Folder > Asset Folder.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_12.png)

После того как APK был добавлен в проект, его нужно загрузить. Есть 2 способа загрузки APK, как описано ниже.

- Загрузите APK в пользовательском классе приложения, используя фрагмент кода ниже, и зарегистрируйте пользовательский класс приложения в файле AndroidManifest.xml.

{{< highlight java >}}

 LibsLoadHelper.loadLibs(this);

{{< /highlight >}}

- Загрузите APK в методе OnCreate MainActivity.

{{< highlight java >}}

 LibsLoadHelper.loadLibs(getApplicationContext());

{{< /highlight >}}

Теперь мы готовы писать код. Чтобы демонстрация была понятной, мы добавили виджет кнопки в макет и собираемся обработать ее событие нажатия, как описано ниже.

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

Когда вы запускаете приложение с помощью кнопки воспроизведения на интерфейсе IDE (или используя SHIFT + F10), эмулятор загрузит приложение, как показано ниже.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_13.png)

Нажатие кнопки на эмуляторе выполнит код для создания новой электронной таблицы во внешней папке хранения эмулятора. Вы можете получить доступ к файлу из монитора устройств Android, как показано ниже.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_14.png)

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_15.png)


