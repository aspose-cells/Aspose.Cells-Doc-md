---
title: Aspose.Cells для Android через установку Java
type: docs
weight: 30
url: /ru/java/aspose-cells-for-android-via-java-installation/
---
## **Системные Требования**
Aspose.Cells для Android через Java не зависит от платформы и может использоваться на любой платформе, на которой установлена среда выполнения Android, и будет работать в системах Android с ОС Android 2.0 или более поздней версии. В настоящее время компонент был протестирован с:

- Андроид 5.1 v22
## **Установите Aspose.Cells для Android через Java из репозитория Maven.**
1. Добавьте репозиторий maven в вашу сборку.gradle
1. Добавьте «Aspose.Cells для Android через Java» JAR в качестве зависимости

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
## **Как использовать Aspose.Cells для Android через Java**
В этом разделе описаны необходимые шаги для настройки Aspose.Cells для Android через Java в Android Studio IDE, при условии, что на вашем компьютере уже установлена последняя версия Android Studio, а также вы приобрели последнюю версию Aspose.Cells для Android через Java. упаковка.

{{% alert color="primary" %}} 

Если вы еще не установили Android Studio, вам необходимо сначала получить установку Android Studio и установить ее на свой компьютер. Вы можете скачать последнюю версию Android Studio с[здесь](https://developer.android.com/studio/index.html#win-bundle) тогда как подробности о том, как установить IDE, доступны[здесь](https://developer.android.com/studio/install.html).

{{% /alert %}} {{% alert color="primary" %}} 

 Aspose.Cells для Android через пакет Java можно загрузить с[здесь](https://downloads.aspose.com/cells/androidjava). Обратите внимание, что каждый пакет выпуска Aspose.Cells для Android через Java в основном состоит из 2 файлов, как описано ниже.

- **aspose-cells-xxxjar** — это основной файл библиотеки, содержащий все пространства имен от Aspose.Cells для Android до Java API.
- **aspose-cells-xxx-libs.apk** это APK, содержащий сторонний файл bcprov-jdk15-146.jar, используемый для средств шифрования и дешифрования, предлагаемых Aspose.Cells для Android через Java API.

{{% /alert %}} 
### **Начало работы с Aspose.Cells для Android через Java в Android Studio**
После загрузки Android Studio IDE нажмите «Файл» > «Создать» > «Новый проект», как показано ниже.

![дело:изображение_альтернативный_текст](aspose-cells-for-android-via-java-installation_1.png)

Вы также можете создать новый проект на экране приветствия Android Studio, как показано ниже.

![дело:изображение_альтернативный_текст](aspose-cells-for-android-via-java-installation_2.png)

Далее вам будет предложено указать имя приложения, домен и место для хранения файлов проекта. Вы можете изменить значения по умолчанию по своему выбору или оставить их такими, какие они есть, и нажать «Далее».

![дело:изображение_альтернативный_текст](aspose-cells-for-android-via-java-installation_3.png)

На следующем шаге вам нужно указать Android-устройство, на котором вы хотите разместить/запустить приложение. После выбора нажмите кнопку «Далее».

![дело:изображение_альтернативный_текст](aspose-cells-for-android-via-java-installation_4.png)

Теперь вам нужно выбрать действие из предопределенного списка шаблонов. Чтобы сделать демонстрацию простой, мы выбрали шаблон «Пустая активность», как показано ниже.

![дело:изображение_альтернативный_текст](aspose-cells-for-android-via-java-installation_5.png)

Нажмите кнопку «Готово» в диалоговом окне «Настройка действия», так как мы сохраним все настройки по умолчанию такими, какие они есть.

![дело:изображение_альтернативный_текст](aspose-cells-for-android-via-java-installation_6.png)

Как только вы нажмете кнопку «Готово» на предыдущем шаге, IDE начнет сборку проекта, как показано ниже. Дайте ему закончить или нажмите кнопку «Отмена».

![дело:изображение_альтернативный_текст](aspose-cells-for-android-via-java-installation_7.png)

Теперь проект загружен в IDE, однако вы можете изменить вид на Project, чтобы просмотреть полную иерархию файлов проекта. Чтобы изменить представление, проверьте следующий снимок.

![дело:изображение_альтернативный_текст](aspose-cells-for-android-via-java-installation_8.png)

 После изменения вида на Project найдите и загрузите**строй.gradle** файл в редакторе и вставьте следующий фрагмент, как показано ниже.

{{< highlight "java" >}}

 dexOptions{

    javaMaxHeapSize "4g"

}

{{< /highlight >}}

![дело:изображение_альтернативный_текст](aspose-cells-for-android-via-java-installation_9.png)

Далее мы добавим в проект Aspose.Cells для Android через Java Jar. Есть 2 важных шага, как подробно описано ниже.

-  Вручную скопируйте файл Aspose.Cells для Android через банку Java в**\приложение\библиотеки** папка.
- Добавьте Aspose.Cells для Android через Java Jar в качестве библиотеки в модуль, как показано ниже.

![дело:изображение_альтернативный_текст](aspose-cells-for-android-via-java-installation_10.png)

Вам будет предложено выбрать модуль, к которому вы хотите добавить Aspose.Cells for Java.Android Jar в качестве библиотеки. Пожалуйста, выберите соответствующий и нажмите OK.

![дело:изображение_альтернативный_текст](aspose-cells-for-android-via-java-installation_11.png)

 Вам также необходимо добавить файл APK в проект. Вы должны скопировать APK на**\приложение\источник\основной\активы**папка. Если у вас нет папки ресурсов в основной папке, вы можете создать ее, щелкнув правой кнопкой мыши основной узел в представлении «Проект». Выберите «Создать» > «Папка» > «Папка ресурсов».

![дело:изображение_альтернативный_текст](aspose-cells-for-android-via-java-installation_12.png)

После того, как APK был добавлен в проект, он должен быть загружен проектом. Есть 2 способа загрузить APK следующим образом.

- Загрузите APK в пользовательский класс приложения, используя приведенный ниже фрагмент кода, и зарегистрируйте пользовательский класс приложения в файле AndroidManifest.xml.

{{< highlight "java" >}}

 LibsLoadHelper.loadLibs(this);

{{< /highlight >}}

- Загрузите APK в методе OnCreate MainActivity.

{{< highlight "java" >}}

 LibsLoadHelper.loadLibs(getApplicationContext());

{{< /highlight >}}

Теперь мы готовы написать код. Чтобы сделать демонстрацию простой для понимания, мы добавили в макет виджет Button и собираемся обрабатывать его событие щелчка следующим образом.

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

Когда вы запускаете приложение с помощью кнопки воспроизведения в интерфейсе IDE (или с помощью SHIFT + F10), эмулятор загрузит приложение, как показано ниже.

![дело:изображение_альтернативный_текст](aspose-cells-for-android-via-java-installation_13.png)

Нажатие кнопки на эмуляторе выполнит код для создания новой электронной таблицы во внешней папке хранилища эмулятора. Вы можете получить доступ к файлу из Android Device Monitor, как показано ниже.

![дело:изображение_альтернативный_текст](aspose-cells-for-android-via-java-installation_14.png)

![дело:изображение_альтернативный_текст](aspose-cells-for-android-via-java-installation_15.png)


