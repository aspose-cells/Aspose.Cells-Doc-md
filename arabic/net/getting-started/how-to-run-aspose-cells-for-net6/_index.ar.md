---
title: كيفية تشغيل Aspose.Cells لـ .Net6
type: docs
description: كيفية تشغيل Aspose.Cells لـ .Net6
weight: 138
url: /ar/net/how-to-run-aspose-cells-for-net6/
---
##  ملخص

 بالنسبة لمنصات .NET6 (أو الأحدث)، قارنها بالأنظمة الأساسية السابقة (.netcore31 أو ما قبلها)، هناك اختلاف مهم يتعلق بمكتبة الرسومات.
 في هذا الرسمي[Microsoft وثيقة](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only)، فهو يوضح أنه بالنسبة لـ .NET6 أو الإصدارات الأحدث، سيتم دعم مكتبة الرسومات "System.Drawing.Common" فقط على Windows، ويقدم توصيات لاستبدال مكتبة الرسومات.

بالنسبة لمنتج Apose.Cells، أجرينا التقييم وأكملنا ترحيل مكتبة الرسومات. نحن نستخدم SkiaSharp بدلاً من System.Drawing.Common في الأنظمة غير Windows، كما هو مقترح في الوثائق الرسمية لـ Microsoft. يرجى ملاحظة أن هذا التغيير الحاسم سيدخل حيز التنفيذ في Aspose.Cells 22.10.1 أو إصدار أحدث لـ .Net6.

بالنسبة إلى .netcore31 أو ما قبله، من أجل التوافق والاستقرار، مازلنا نستخدم حاليًا مكتبة الرسومات "System.Drawing.Common". تبعيات .netcore31 أو ما قبله هي كما يلي:
- System.Drawing.Common، 4.7.0.
- System.Security.Cryptography.Pkcs, 5.0.1.
- System.Text.Encoding.CodePages، 4.7.0.

##  قم بتشغيل Aspose.Cells لـ .Net6 على Windows

أولاً، يمكنك إنشاء تطبيق ‎.net6 باستخدام VS2022، ثم يمكنك اختيار خيارات التثبيت التالية:

###  التثبيت من خلال nuget

1.  ابحث عن Aspose.Cells من NuGet:[Aspose.Cells for .NET NuGet الباقة](https://www.nuget.org/packages/Aspose.Cells/). 
يمكنك أيضًا تثبيت Aspose.Cells من مدير الحزم Nuget في VS2022.

2. سيتم تثبيت "SkiaSharp" أو "System.Drawing.Common" تلقائيًا باعتباره تبعية لـ Aspose.Cells 22.10.1 أو أحدث لمنصات .Net6، والتي تعتمد على تكوين "Target OS" في مشروعك.
- قم بتعيين "Target OS" على "Windows" لمشروعك، وسوف تستخدم "System.Drawing.Common" كاعتماد على نظام Windows الخاص بك لمشروع .Net6. في هذا التكوين، تكون نتيجة الرسم أقرب إلى ‎.netcore31 أو قبله.
**![تكوين نظام التشغيل المستهدف](TargetOS.png)**
-  اضبط "Target OS" على "None" أو الخيارات الأخرى لمشروعك، وسوف تستخدم "SkiaSharp" كاعتماد على نظام Windows الخاص بك لمشروع .Net6.*يرجى ملاحظة أن الإصدار الذي يستخدم "SkiaSharp" باعتباره تبعية لا يدعم ميزة الطباعة إلى الطابعة.*

###  التثبيت من خلال MSI أو DLL

1. [تنزيل Aspose.Cells.msi أو DLL](https://releases.aspose.com/cells/net/)

2. افتح دليل التثبيت أو دليل DLL، ثم حدد الخطوة 3 أو 4 أدناه:

3. حدد موقع الدليل الفرعي "net6.0-windows"، وأضف الملف Aspose.Cells.dll فيه إلى تطبيق .net6 الخاص بك. أضف حزم nuget التالية يدويًا إلى مشروع .net6 الخاص بك:
- System.Drawing.Common، 4.7.0.
- System.Security.Cryptography.Pkcs, 6.0.3.
- System.Text.Encoding.CodePages، 4.7.0.

بهذه الطريقة، ستستخدم "System.Drawing.Common" كاعتماد على نظام Windows الخاص بك لمشروع .Net6. في هذا التكوين، تكون نتيجة الرسم أقرب إلى ‎.netcore31 أو قبله.

4. حدد موقع الدليل الفرعي "net6.0"، وأضف الملف Aspose.Cells.dll فيه إلى تطبيق .net6 الخاص بك. أضف حزم nuget التالية يدويًا إلى مشروع .net6 الخاص بك:
- سكياشارب، 2.88.6.
- System.Security.Cryptography.Pkcs, 6.0.3.
- System.Text.Encoding.CodePages، 4.7.0.

 بهذه الطريقة، ستستخدم "SkiaSharp" كاعتماد على نظام Windows الخاص بك لمشروع .Net6.*يرجى ملاحظة أن الإصدار الذي يستخدم "SkiaSharp" باعتباره تبعية لا يدعم ميزة الطباعة إلى الطابعة.*
##  قم بتشغيل Aspose.Cells لـ .Net6 على Linux

راجع طريقة التثبيت على الرقم Windows، يمكنك فقط اختيار SkiaSharp كمكتبة رسومات تابعة لنظام Linux.

يتعين عليك القيام بالعمليات الإضافية التالية لضمان الاستخدام السليم لـ SkiaSharp في نظام التشغيل Linux:

1. قم بتشغيل الأمر التالي في نظام Linux الخاص بك:
```
apt-get update && apt-get install -y libfontconfig1
```
OR
```
apk update && apk add fontconfig 
```

2. أضف حزم nuget "SkiaSharp.NativeAssets.Linux 2.88.6" إلى مشروع .net6 الخاص بك.

3. أو يمكنك اختيار إضافة حزم nuget "SkiaSharp.NativeAssets.Linux.NoDependeency 2.88.6" إلى مشروع .net6 الخاص بك، بدلاً من الخطوتين أعلاه.

###  مثال Dockerfile لأوبونتو

1. أضف حزم nuget "SkiaSharp.NativeAssets.Linux 2.88.6" إلى مشروع .net6 الخاص بك.

2. استخدم ملف Dockerfile التالي:
{{< highlight "plain" >}}
#  Ubuntu 20.04
FROM mcr.microsoft.com/dotnet/runtime:6.0-focal AS base
WORKDIR /app

#  add "libfontconfig1" package if using "SkiaSharp.NativeAssets.Linux" in your project
#  Or you need to use "SkiaSharp.NativeAssets.Linux.NoDependencies" in your project
RUN apt-get update && apt-get install -y libfontconfig1

#  Copy fonts from local to docker
#  For example, put a "fonts" folder in your project folder, and put the font files in it,
#  then, use the following line:
COPY fonts/ /usr/share/fonts

FROM mcr.microsoft.com/dotnet/sdk:6.0-focal AS build
WORKDIR /src
COPY ["Ubuntu_Docker.csproj", "."]
RUN dotnet restore "./Ubuntu_Docker.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "Ubuntu_Docker.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ubuntu_Docker.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ubuntu_Docker.dll"]
{{< /highlight >}}

###  مثال Dockerfile لجبال الألب

1. أضف حزم nuget "SkiaSharp.NativeAssets.Linux 2.88.6" إلى مشروع .net6 الخاص بك.

2. استخدم ملف Dockerfile التالي:
{{< highlight "plain" >}}
# Alpine 3.16
FROM mcr.microsoft.com/dotnet/runtime:6.0-alpine3.16 AS base
WORKDIR /app

#  add "fontconfig" package if using "SkiaSharp.NativeAssets.Linux" in your project
#  Or you need to use "SkiaSharp.NativeAssets.Linux.NoDependencies" in your project
RUN apk update && apk add fontconfig 

#  Copy fonts from local to docker
#  For example, put a "fonts" folder in your project folder, and put the font files in it,
#  then, use the following line:
COPY fonts/ /usr/share/fonts

FROM mcr.microsoft.com/dotnet/sdk:6.0-alpine3.16 AS build
WORKDIR /src
COPY ["Alpine_Docker.csproj", "."]
RUN dotnet restore "./Alpine_Docker.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "Alpine_Docker.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Alpine_Docker.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Alpine_Docker.dll"]
{{< /highlight >}}
