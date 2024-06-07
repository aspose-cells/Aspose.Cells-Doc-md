---
title: 通过Java安装Aspose.Cells for Android
type: docs
weight: 30
url: /zh/java/aspose-cells-for-android-via-java-installation/
---

## **系统要求**
通过Java的Aspose.Cells for Android 是独立于平台的，可在已安装Android Runtime环境且运行Android OS 2.0或更高版本的任何平台上使用，并可在运行Android OS的Android系统上运行。截至目前，该组件已通过以下系统进行了测试:

- Android 5.1 v 22
## **从Maven仓库安装通过Java的Aspose.Cells for Android**
1. 将maven仓库添加到您的**build.gradle**中 
1. 将'Aspose.Cells for Android via Java' JAR添加为依赖项

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
## **如何在Android Studio中使用通过Java的Aspose.Cells for Android**
本主题将指导您完成在Android Studio IDE中设置Aspose.Cells for Android via Java 的必要步骤，假设您已将最新版本的Android Studio安装在您的计算机上，并且也已获得了通过Java的最新版本的Aspose.Cells for Android package。

{{% alert color="primary" %}} 

如果您尚未安装Android Studio，则必须首先获取Android Studio的设置并在您的计算机上安装它。您可以从[这里](https://developer.android.com/studio/index.html#win-bundle)下载最新版本的Android Studio，有关如何安装IDE的详细信息可在[此处](https://developer.android.com/studio/install.html)找到。

{{% /alert %}} {{% alert color="primary" %}} 

通过[此处](https://downloads.aspose.com/cells/androidjava)下载通过Java的Aspose.Cells for Android package。请注意，每个通过Java的Aspose.Cells for Android package的发布包主要包含以下2个文件。

- **aspose-cells-x.x.x.jar** 是包含通过Java的Aspose.Cells for Android API所有命名空间的主要库文件。
- **aspose-cells-x.x.x-libs.apk** 是APK，包含用于加密和解密功能的第三方bcprov-jdk15-146.jar，由通过Java的Aspose.Cells for Android API提供。

{{% /alert %}} 
### **在Android Studio中开始使用通过Java的Aspose.Cells for Android**
一旦Android Studio IDE加载，点击文件 > 新建 > 新项目，如下所示。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_1.png)

您还可以从Android Studio的欢迎屏幕中创建新项目，如下所示。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_2.png)

接下来，您将被提示指定应用程序名称、域和存储项目文件的位置。您可以选择根据需要更改默认值或将其保持不变，然后点击下一步。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_3.png)

在下一步中，您必须指定要托管/运行您的应用程序的Android设备。一旦选择，点击下一步按钮。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_4.png)

现在，您需要从预定义模板列表中选择Activity。为了使演示简单，我们选择了空Activity模板，如下所示。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_5.png)

在自定义Activity对话框上点击完成按钮，因为我们将保留所有默认设置。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_6.png)

一旦您在上一步中点击完成按钮，IDE将开始构建项目，如下所示。让其完成或点击取消按钮。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_7.png)

现在项目已在IDE中加载，但您可能需要将视图更改为Project，以便查看项目文件的完整层次结构。要更改视图，请参考以下快照。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_8.png)

将视图更改为Project后，在编辑器中找到并加载**build.gradle**文件，然后粘贴以下代码片段，如下所示。

{{< highlight java >}}

 dexOptions{

    javaMaxHeapSize "4g"

}

{{< /highlight >}}

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_9.png)

接下来，我们将将通过Java的Aspose.Cells for Android Jar添加到项目中。下面详细介绍了2个重要步骤。

- 将通过Java的Aspose.Cells for Android Jar手动复制到**\app\libs**文件夹中。
- 将通过Java的Aspose.Cells for Android Jar作为库添加到模块中，如下所示。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_10.png)

您将被提示选择要将Aspose.Cells for Java.Android Jar添加为库的模块。 请选择适当的选项，然后单击确定。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_11.png)

您还需要将APK文件添加到项目中。 您必须将APK复制到**\app\src\main\assets**文件夹中。 如果在main文件夹下没有assets文件夹，您可以通过在项目视图中右键单击main节点，选择新建 > 文件夹 > 资源文件夹 来创建一个。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_12.png)

一旦将APK添加到项目中，项目需要加载它。 有两种加载APK的方法如下。

- 使用下面提供的片段在自定义应用程序类中加载APK，并将自定义应用程序类注册到AndroidManifest.xml中。

{{< highlight java >}}

 LibsLoadHelper.loadLibs(this);

{{< /highlight >}}

- 在MainActivity的OnCreate方法中加载APK。

{{< highlight java >}}

 LibsLoadHelper.loadLibs(getApplicationContext());

{{< /highlight >}}

现在我们准备编写代码。 为了使演示易于理解，我们已将一个Button小部件添加到布局中，并将处理其点击事件如下。

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

当您使用IDE界面上的播放按钮（或使用SHIFT + F10）运行应用程序时，模拟器将加载应用程序如下所示。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_13.png)

在模拟器上单击按钮将执行代码以在模拟器的外部存储文件夹中创建新的电子表格。 您可以如下图所示从Android设备监视器中访问该文件。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_14.png)

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_15.png)


