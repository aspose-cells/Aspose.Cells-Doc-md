---
title: Aspose.Cells for Android via Java 安装
type: docs
weight: 30
url: /zh/java/aspose-cells-for-android-via-java-installation/
---
## **系统要求**
Aspose.Cells for Android via Java 与平台无关，可以在安装了 Android 运行时环境的任何平台上使用，并将在运行 Android OS 2.0 或更高版本的 Android 系统上运行。目前，该组件已通过以下测试：

- 安卓 5.1 v 22
## **从 Maven 存储库安装 Aspose.Cells for Android via Java**
1. 将 maven 存储库添加到您的 build.gradle
1. 添加 'Aspose.Cells for Android via Java' JAR 作为依赖项

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
## **如何使用 Aspose.Cells for Android via Java**
本主题将指导您完成在 Android Studio IDE 中设置 Aspose.Cells for Android via Java 的必要步骤，假设您已经在您的计算机上安装了最新版本的 Android Studio，并且您还获得了最新版本的 Aspose.Cells for Android via Java 包。

{{% alert color="primary" %}} 

如果您还没有安装 Android Studio，则必须先获取 Android Studio 的安装程序并将其安装到您的机器上。您可以从以下位置下载最新版本的 Android Studio[这里](https://developer.android.com/studio/index.html#win-bundle)而有关如何安装 IDE 的详细信息可用[这里](https://developer.android.com/studio/install.html).

{{% /alert %}} {{% alert color="primary" %}} 

Aspose.Cells for Android via Java 包可以从下载[这里](https://downloads.aspose.com/cells/androidjava).请注意，Aspose.Cells for Android via Java 的每个发布包主要由以下2个文件组成。

- **aspose-细胞-xxxjar**是包含 Aspose.Cells for Android via Java API 的所有命名空间的主库文件。
- **aspose-细胞-xxx-libs.apk**是包含第 3 方 bcprov-jdk15-146.jar 的 APK，用于 Aspose.Cells for Android via Java API 提供的加密和解密设施。

{{% /alert %}} 
### **Android Studio Aspose.Cells for Android via Java 入门**
加载 Android Studio IDE 后，单击文件 > 新建 > 新建项目，如下所示。

![待办事项：图片_替代_文本](aspose-cells-for-android-via-java-installation_1.png)

您还可以从 Android Studio 的欢迎屏幕创建一个新项目，如下所示。

![待办事项：图片_替代_文本](aspose-cells-for-android-via-java-installation_2.png)

接下来，系统将提示您指定应用程序名称、域和存储项目文件的位置。您可以选择根据您的选择更改默认值或让它们保持原样，然后单击下一步。

![待办事项：图片_替代_文本](aspose-cells-for-android-via-java-installation_3.png)

在下一步中，您必须指定希望托管/运行应用程序的 Android 设备。选择后，单击下一步按钮。

![待办事项：图片_替代_文本](aspose-cells-for-android-via-java-installation_4.png)

现在您需要从预定义的模板列表中选择活动。为了保持演示简单，我们选择了 Empty Activity 模板，如下所示。

![待办事项：图片_替代_文本](aspose-cells-for-android-via-java-installation_5.png)

单击 Customize the Activity 对话框中的 Finish 按钮，因为我们将保留所有默认设置。

![待办事项：图片_替代_文本](aspose-cells-for-android-via-java-installation_6.png)

只要您在上一步中单击“完成”按钮，IDE 就会开始构建项目，如下所示。让它完成或单击取消按钮。

![待办事项：图片_替代_文本](aspose-cells-for-android-via-java-installation_7.png)

现在项目已加载到 IDE 中，但是，您可能希望将视图更改为项目，以便可以查看项目文件的完整层次结构。要更改视图，请检查以下快照。

![待办事项：图片_替代_文本](aspose-cells-for-android-via-java-installation_8.png)

将视图更改为项目后，找到并加载**build.gradle**编辑器中的文件并粘贴以下代码段，如下所示。

{{< highlight "java" >}}

 dexOptions{

    javaMaxHeapSize "4g"

}

{{< /highlight >}}

![待办事项：图片_替代_文本](aspose-cells-for-android-via-java-installation_9.png)

接下来，我们将 Aspose.Cells for Android via Java Jar 添加到项目中。有 2 个重要步骤，详述如下。

- 手动复制Aspose.Cells for Android via Java Jar到**\应用\库**文件夹。
- 将 Aspose.Cells for Android via Java Jar 作为库添加到模块中，如下所示。

![待办事项：图片_替代_文本](aspose-cells-for-android-via-java-installation_10.png)

系统将提示您选择要将 Aspose.Cells for Java.Android Jar 作为库添加到的模块。 Please choose appropriately and click OK.

![待办事项：图片_替代_文本](aspose-cells-for-android-via-java-installation_11.png)

您还需要将 APK 文件添加到项目中。您必须将 APK 复制到**\app\src\main\assets**文件夹。如果主文件夹下没有资产文件夹，可以通过在项目视图中右键单击主节点来创建一个。选择新建 > 文件夹 > 资产文件夹。

![待办事项：图片_替代_文本](aspose-cells-for-android-via-java-installation_12.png)

将 APK 添加到项目后，需要由项目加载它。有两种加载 APK 的方法如下。

- 使用下面提供的代码片段将 APK 加载到自定义应用程序类中，并将自定义应用程序类注册到 AndroidManifest.xml。

{{< highlight "java" >}}

 LibsLoadHelper.loadLibs(this);

{{< /highlight >}}

- 在 MainActivity 的 OnCreate 方法中加载 APK。

{{< highlight "java" >}}

 LibsLoadHelper.loadLibs(getApplicationContext());

{{< /highlight >}}

现在我们准备好编写代码了。为了使演示易于理解，我们在布局中添加了一个 Button 小部件，并将按如下方式处理其点击事件。

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

当您使用 IDE 界面上的播放按钮（或使用 SHIFT + F10）运行应用程序时，模拟器将加载应用程序，如下所示。

![待办事项：图片_替代_文本](aspose-cells-for-android-via-java-installation_13.png)

单击模拟器上的按钮将执行代码以在模拟器的外部存储文件夹中创建一个新的电子表格。您可以从 Android 设备监视器访问该文件，如下所示。

![待办事项：图片_替代_文本](aspose-cells-for-android-via-java-installation_14.png)

![待办事项：图片_替代_文本](aspose-cells-for-android-via-java-installation_15.png)


