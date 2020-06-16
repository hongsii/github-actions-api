# Github actions api for heroku


### GET /github/:owner/:repo/deployments

deployment 이벤트로 action을 실행시키는 API

**Request**

```
GET localhost:8080/github/hongsii/github-actions-api/deployments?branch=master&token=PERSONAL_ACCESS_TOKEN
```

** Parameters **
* branch : 실행할 브랜치 ex) master, develop...
* token : Github personal access token 
  - [토큰 생성 방법](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line)
  - 필수 권한 : `repo > repo_deployment`
