---
title: Aspose.Cells for Android via Java安装
type: docs
weight: 30
url: /zh/java/aspose-cells-for-android-via-java-installation/
---

## **系统要求**
Aspose.Cells for Android via Java 与平台无关，可以在已安装安卓运行环境的任何平台上使用，并且将在运行Android OS 2.0或更高版本的Android系统上运行。目前，该组件已经与以下系统进行了测试：

- Android 5.1 v 22
## **从Maven仓库安装Aspose.Cells for Android via Java**
1. 在你的build.gradle中加入Maven仓库 
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
## **如何使用Aspose.Cells for Android via Java**
本主题将指导你完成在Android Studio IDE中设置Aspose.Cells for Android via Java的必要步骤，假设你已经在你的设备上安装了最新版本的Android Studio，并且也已经获取了最新版本的Aspose.Cells for Android via Java包。

{{% alert color="primary" %}} 

如果你还没有安装Android Studio，你需要首先获取Android Studio的设定并将其安装在你的设备上。你可以从[这里](https://developer.android.com/studio/index.html#win-bundle)下载最新版本的Android Studio，而有关如何安装这个IDE的详细信息可以在[这里](https://developer.android.com/studio/install.html)找到。

{{% /alert %}} {{% alert color="primary" %}} 

Aspose.Cells for Android via Java包可以从[这里](https://downloads.aspose.com/cells/androidjava)下载。请注意，Aspose.Cells for Android via Java的每个发布包主要包含以下2个文件的详细信息。

- **aspose-cells-x.x.x.jar**是主库文件，包含Aspose.Cells for Android via Java API的所有命名空间。
- **aspose-cells-x.x.x-libs.apk**是包含Aspose.Cells for Android via Java API提供的加密和解密设施所使用的第三方bcprov-jdk15-146.jar的APK。

{{% /alert %}} 
### **在Android Studio中开始使用Aspose.Cells for Android via Java**
一旦Android Studio IDE加载完成，点击文件 > 新建 > 新建项目如下所示。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_1.png)

你也可以从Android Studio的欢迎界面创建新项目如下所示。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_2.png)

接下来，你将被提示指定应用程序名称、域名和存储项目文件的位置。你可以选择根据自己的选择更改默认值，或者保持默认值不变，然后点击下一步。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_3.png)

在下一步中，你需要指定你希望托管/运行你的应用程序的Android设备。一旦选择，点击下一步按钮。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_4.png)

现在你需要从预定义的模板列表中选择Activity。为了保持演示简单，我们选择了空Activity模板如下所示。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_5.png)

如示例所示，点击自定义Activity对话框上的完成按钮，因为我们将保持所有默认设置不变。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_6.png)

在上一步中点击完成按钮后，IDE将开始构建项目如下所示。让它完成或者点击取消按钮。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_7.png)

现在项目已经在IDE中加载，但是你可能希望将视图更改为项目，这样你就可以查看项目文件的完整层次结构。为了更改视图，请参考下面的截图。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_8.png)

将视图更改为项目后，在编辑器中找到并加载**build.gradle**文件，并粘贴以下代码段如下所示。

{{< highlight java >}}

 dexOptions{

    javaMaxHeapSize "4g"

}

{{< /highlight >}}

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_9.png)

接下来，我们将添加Aspose.Cells for Android via Java Jar到项目中。有以下两个重要步骤详细说明。

- 将 Aspose.Cells for Android via Java Jar 手动复制到 **\app\libs** 文件夹。
- 将 Aspose.Cells for Android via Java Jar 添加为模块中的库，如下所示。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_10.png)

您将被提示选择要将 Aspose.Cells for Java Android Jar 作为库添加到的模块。 请选择适当的选项，然后单击“确定”

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_11.png)

您还需要将 APK 文件添加到项目中。您必须将 APK 复制到 **\app\src\main\assets** 文件夹。如果主文件夹下没有 assets 文件夹，则可以通过在项目视图中右键单击主节点来创建一个。选择 新建 > 文件夹 > 资产文件夹。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_12.png)

一旦将 APK 添加到项目中，项目就需要加载它。有两种方式加载 APK，如下所示。

- 在自定义应用程序类中加载 APK，使用下面提供的代码片段，并将自定义应用程序类注册到 AndroidManifest.xml。

{{< highlight java >}}

 LibsLoadHelper.loadLibs(this);

{{< /highlight >}}

- 在 MainActivity 的 OnCreate 方法中加载 APK。

{{< highlight java >}}

 LibsLoadHelper.loadLibs(getApplicationContext());

{{< /highlight >}}

现在，我们已准备好编写代码了。为了使演示易于理解，我们已在布局中添加了一个按钮微件，并将处理其单击事件如下。

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

当使用 IDE 界面上的播放按钮运行应用程序（或使用 SHIFT + F10），模拟器将加载应用程序如下所示。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_13.png)

在模拟器上单击按钮将执行代码，以在模拟器的外部存储文件夹中创建一个新的电子表格。您可以如下访问 Android 设备监视器中的文件。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_14.png)

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_15.png)


