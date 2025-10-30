---
title: GridJsを使ったコラボレーティブなExcelエディタの構築方法
type: docs
weight: 260
url: /ja/java/aspose-cells-gridjs/how-to-build-collaborative-excel-editor/
keywords: GridJs,コラボレーティブ,エクセルエディタ,スプレッドシート,Java
description: この記事では、Aspose.Cells.GridJs for Javaを使用したコラボレーティブExcelエディタの構築方法を紹介します。
aliases:
  - /java/aspose-cells-gridjs/collaborative-editor/
  - /java/aspose-cells-gridjs/how-to-build-collaborative-spreadsheet-editor/
  - /java/aspose-cells-gridjs/how-to-build-collaborative-excel-editor-using-gridjs/
---

# コラボレーティブExcelエディタガイド

## アーキテクチャ概要

以下の図は、GridJsが複数のユーザーによる共同編集を可能にする仕組みを示しています。 
Spring Bootのバックエンド、WebSocket通信、および状態管理用のMySQLデータベースを備えています。

![GridJsコラボレーティブアーキテクチャ](gridjs_collaborative_architecture.png)

## 前提条件

開始前に、以下をインストールしていることを確認してください：

- **Java 8以上**  
- **Maven**  
- **MySQL**（または他のサポートされているSQLデータベース）  
- （任意）**Docker**（コンテナでの実行を好む場合）  
- 有効な**Aspose.Cellsライセンス**（または[一時的なライセンス](https://purchase.aspose.com/temporary-license)）  

---

## Step 1: Clone the Demo Project

Clone the official [Aspose.Cells GridJs demo repository](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/master/Examples.GridJs.Collaborative):

```bash
git clone https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java.git
cd Aspose.Cells-for-Java/Examples.GridJs.Collaborative
```

---

## Step 2: Configure Collaborative Mode

Open the [`src/main/resources/application.properties`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/resources/application.properties) file and adjust the settings:

```properties
# Directory containing spreadsheet files
testconfig.ListDir=/app/wb

# Directory for storing cache files
testconfig.CachePath=/app/grid_cache

# Aspose.Cells license file
testconfig.AsposeLicensePath=/app/license

# Enable collaborative mode
gridjs.iscollabrative=true

# Database connection (example: MySQL)
spring.datasource.url=jdbc:mysql://localhost:3306/gridjsdemodb?createDatabaseIfNotExist=true&useUnicode=true&serverTimezone=UTC&useSSL=false
spring.datasource.username=root
spring.datasource.password=root
spring.sql.init.platform=mysql
```

これにより、複数のユーザーが同じスプレッドシートを同時に編集できます。  
変更はデータベースに保存され、リアルタイムでクライアント間で同期されます。

---

## Step 3: Run the Application

Run with Maven:

```bash
mvn spring-boot:run
```

直接メインクラスから：

```
src/main/java/com/aspose/gridjsdemo/usermanagement/UserManagementApplication.java
```

---

## Step 4: Test Collaborative Editing

Open your browser and navigate to:  
👉 `http://localhost:8080/gridjsdemo/list`

Steps:

1. A login page appears. Click **Create User** to register User1 and log in. You will then see the file list.  
2. Open a file from the list. The spreadsheet editor will load.  
3. Copy the same URL into another browser window. It will redirect to the login page. Create User2 and log in.  
4. Both users now see the same spreadsheet.  
5. If User1 edits the spreadsheet, User2 will see the changes in real time.  
6. If User2 edits, User1 will see the changes as well.  
7. Users can also download and save the file.  

---

## ステップ5：Dockerで実行（任意）

Dockerで実行する場合は、[`docker-compose.yml`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/docker-compose.yml)の10行目を編集して、ライセンスファイルをマッピングします。  

例として、ライセンスファイルが `C:/license/aspose.lic` にある場合：

```yaml
volumes:
  - C:/license/aspose.lic:/app/license  # optional: set Aspose license file
```

これにより、ローカルのファイルがコンテナにマップされます。

次にビルドして実行：

```bash
docker-compose up --build
```

アプリにアクセス：  
👉 `http://localhost:8080/gridjsdemo/list`

---

## Key Configuration Details

### 1. Enable Collaborative Mode

In [`/src/main/resources/application.properties`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/resources/application.properties):

```properties
gridjs.iscollabrative=true
```

サーバー側の設定 [`/src/main/java/com/aspose/gridjsdemo/filemanagement/FileConfig.java`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/java/com/aspose/gridjsdemo/filemanagement/FileConfig.java):

```java
@Bean
public GridJsOptions gridJsOptions() {
    //..... other options
    //here we shall set true for collaborative mode
    options.setCollaborative(true);
    return options;
}
```

またはグローバル：

```java
Config.setCollaborative(true);
```

クライアント側のロードオプション [`/src/main/resources/templates/file/index.html`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/resources/templates/file/index.html):

```js
const option = {
    //..... other options
    //here we shall set true for collaborative mode
    isCollaborative: true
    //..... other options
};
```

---

### 2. User System Integration

The demo uses **Spring Security** for a simple user system.  

You must provide a `CoWorkUserProvider` implementation to connect GridJs with your user system:

In server-side config [`/src/main/java/com/aspose/gridjsdemo/filemanagement/FileConfig.java`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/java/com/aspose/gridjsdemo/filemanagement/FileConfig.java):

For example: here we defined MyCustomUser to implement all the interfaces in CoWorkUserProvider.

```java
@Bean
public CoWorkUserProvider currentUserProvider() {
    return new MyCustomUser();
}
```


[`/src/main/java/com/aspose/gridjsdemo/filemanagement/MyCustomUser.java`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/java/com/aspose/gridjsdemo/filemanagement/MyCustomUser.java):

```java
public class MyCustomUser implements CoWorkUserProvider {
    //Get the current login user name
    @Override
    public String getCurrentUserName() {
        return getCurrentUser().getUsername();
    }

    //Get the current login user Id
    @Override
    public Long getCurrentUserId() {
        return getCurrentUser().getUserId();
    }

    //Get the current login user permission
    @Override
    public CoWorkUserPermission getPermission() {
        return CoWorkUserPermission.EDITABLE;
    }

    private static CustomUserDetails getCurrentUser() {
        Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
        if (authentication != null && authentication.getPrincipal() instanceof CustomUserDetails) {
            return (CustomUserDetails) authentication.getPrincipal();
        }
        throw new IllegalStateException("User not authenticated");
    }
}
```

---

### 3. WebSocket Configuration

The demo uses **Spring WebSocket** with STOMP.  

Example config:

In [`/src/main/java/com/aspose/gridjsdemo/messages/WebSocketConfig.java`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/java/com/aspose/gridjsdemo/messages/WebSocketConfig.java):

```java
public class WebSocketConfig implements WebSocketMessageBrokerConfigurer {
    @Override
    public void configureMessageBroker(MessageBrokerRegistry config) {
        config.enableSimpleBroker("/topic");
        config.setApplicationDestinationPrefixes("/app");
        config.setUserDestinationPrefix("/user");
    }

    @Override
    public void registerStompEndpoints(StompEndpointRegistry registry) {
        registry.addEndpoint("/ws")
                .setAllowedOrigins("http://localhost:8080")
                .withSockJS();
    }
}
```

GridJsは `messageTopic` がデフォルトの "/topic/opr" に一致することを期待しています：

```java
com.aspose.gridjs.Config.setMessageTopic("/topic/opr");
```

または：

```java
@Bean
    public GridJsOptions gridJsOptions() {
	//.... other options
    	options.setMessageTopic("/topic/opr");
    	//.... other options
        return options;
    }
```

クライアント側で：

```js
xs.setCollaborativeSetting('/GridJs2/msg','/ws','/app/opr','/user/queue','/topic/opr');
```

ここでは、 `/GridJs2/msg` は定義されたルートパスに対応します：  
[`src/main/java/com/aspose/gridjsdemo/filemanagement/controller/GridJsOprController.java`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/java/com/aspose/gridjsdemo/filemanagement/controller/GridJsOprController.java):

```java
@RequestMapping("/GridJs2/msg")
```

#### カスタムWebSocketパスの例

サーバーが異なる設定を使用している場合：

```java
public class WebSocketConfig implements WebSocketMessageBrokerConfigurer {
    @Override
    public void configureMessageBroker(MessageBrokerRegistry config) {
        config.enableSimpleBroker("/topic_gridjs");
        config.setApplicationDestinationPrefixes("/app_gridjs");
        config.setUserDestinationPrefix("/user_gridjs");
    }

    @Override
    public void registerStompEndpoints(StompEndpointRegistry registry) {
        registry.addEndpoint("/ws_gridjs")
                .setAllowedOrigins("http://localhost:8080")
                .withSockJS();
    }
}
```

その場合は次のように設定する必要があります：

**サーバー側**：

```java
com.aspose.gridjs.Config.setMessageTopic("/topic_gridjs/opr");
```

または

```java
    @Bean
    public GridJsOptions gridJsOptions() {
	//.... other option
    	options.setMessageTopic("/topic_gridjs/opr");
    	//.... other option
        return options;
    }
```

**クライアント側**：

```js
xs.setCollaborativeSetting('/GridJs2/msg','/ws_gridjs','/app_gridjs/opr','/user_gridjs/queue','/topic_gridjs/opr');
```

setCollaborativeSetting の詳細ドキュメントはこちらで見つけることができます [here](https://docs.aspose.com/cells/java/aspose-cells-gridjs/how-to-use-gridjs-client-api/)

> ⚠️ 注意：デフォルトでは、デモの設定はすぐに動作します。  
追加の設定は、アプリがWebSocketエンドポイントをカスタマイズする場合にのみ必要です。  

また、覚えておいてください：コラボレーティブモードは**遅延読み込み**をサポートしていません。  
`Config.setLazyLoading(true)`を有効にしないでください。

---

## Additional Notes


- We can add **file uploads** to load and edit spreadsheet file from upload directory.  
- Integrate with **cloud storage** like AWS S3 or Azure Blob.  

---

## 結論

Aspose.Cells.GridJsを使用すると、強力な**コラボレーティブExcelエディタ**を迅速に構築できます。  
Javaバックエンド、GridJsフロントエンド、SQLストレージ、WebSocketメッセージングの組み合わせにより、信頼性の高いリアルタイムのスプレッドシート編集が可能になります。

---

## Resources

- [Product Page](https://products.aspose.com/cells/java)  
- [Documentation](https://docs.aspose.com/cells/java/aspose-cells-gridjs/)  
- [API Reference](https://reference.aspose.com/cells/java/com.aspose.gridjs/)  
- [Support Forum](https://forum.aspose.com/c/cells)  
- [Free Online Apps](https://products.aspose.app/cells/family)  
