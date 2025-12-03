# Git Rebase 실습 가이드

이 가이드는 `test2` 디렉토리에서 **Rebase**의 개념을 이해하고 직접 실습해보기 위해 만들어졌습니다.

## 1. Merge vs Rebase: 무엇이 다른가요?

두 브랜치를 합치는 방법은 크게 두 가지가 있습니다.

### Merge (병합)
*   **특징**: "있는 그대로 합친다."
*   **동작**: 두 브랜치의 변경 내용을 모두 유지하며, 두 갈래가 합쳐지는 **새로운 커밋(Merge Commit)**을 만듭니다.
*   **장점**: 히스토리가 있는 그대로 보존되어 어떤 일이 있었는지 정확히 알 수 있습니다.
*   **단점**: 브랜치가 많아지면 히스토리가 복잡해지고 지저분해 보일 수 있습니다. (기차 선로가 꼬인 모양)

### Rebase (재배치)
*   **특징**: "베이스(뿌리)를 다시 심는다."
*   **동작**: 내 브랜치의 시작점(Base)을 최신 `main` 브랜치의 끝으로 옮겨서, 마치 **처음부터 최신 `main` 위에서 작업한 것처럼** 만듭니다.
*   **장점**: 히스토리가 **일직선**으로 깔끔하게 정리됩니다.
*   **단점**: 커밋의 해시값(ID)이 바뀌므로, 이미 원격에 올린 커밋을 Rebase 하면 꼬일 수 있습니다. (혼자 작업할 때 주로 사용)

---

## 2. 실습 준비 (Setup)

`test2` 디렉토리에서 새로운 Git 저장소를 만들고 상황을 세팅합니다.

1.  **디렉토리 생성 및 이동**:
    ```bash
    mkdir -p ~/test2
    cd ~/test2
    ```

2.  **Git 초기화 및 기본 파일 생성**:
    ```bash
    git init
    echo "Base content" > base.py
    git add base.py
    git commit -m "Initial commit: base.py"
    ```

---

## 3. Rebase 실습 시나리오

상황: `main` 브랜치와 `feature` 브랜치가 서로 다른 작업을 해서 갈라진 상태를 만듭니다.

### 1단계: 분기점 만들기

1.  **`feature` 브랜치 생성 및 작업**:
    ```bash
    git checkout -b feature
    echo "Feature work" >> base.py
    git add base.py
    git commit -m "Feature work done"
    ```

2.  **`main` 브랜치로 돌아와서 다른 작업**:
    ```bash
    git checkout main
    echo "Main work" >> base.py
    git add base.py
    git commit -m "Main work done"
    ```

3.  **현재 상태 확인 (로그)**:
    ```bash
    git log --graph --oneline --all
    ```
    *갈라진 그래프(Y자 모양)가 보여야 합니다.*

### 2단계: Rebase 수행

이제 `feature` 브랜치의 뿌리를 `main`의 최신 커밋 뒤로 옮깁니다.

1.  **`feature` 브랜치로 이동**:
    ```bash
    git checkout feature
    ```

2.  **Rebase 실행**:
    ```bash
    git rebase main
    ```

### 3단계: 충돌 해결 (Conflict Resolution)

위에서 같은 파일(`base.py`)을 수정했으므로 **충돌**이 발생할 것입니다. 당황하지 마세요!

1.  **충돌 확인**: `base.py` 파일을 엽니다.
    ```python
    Base content
    <<<<<<< HEAD
    Main work
    =======
    Feature work
    >>>>>>> ...
    ```

2.  **수정**: 원하는 대로 코드를 정리합니다. (예: 둘 다 남기기)
    ```python
    Base content
    Main work
    Feature work
    ```
    *저장하고 닫습니다.*

3.  **Rebase 계속 진행**:
    ```bash
    git add base.py
    git rebase --continue
    ```
    *(커밋 메시지 수정 창이 뜨면 그대로 저장하고 닫으세요.)*

### 4단계: 결과 확인 및 마무리

1.  **로그 확인**:
    ```bash
    git log --graph --oneline --all
    ```
    *아까와 달리 그래프가 **일직선**으로 바뀐 것을 확인하세요!*

2.  **Main에 합치기 (Fast-forward)**:
    이제 `feature`가 `main`의 앞쪽에 일직선으로 있으므로, 깔끔하게 합쳐집니다.
    ```bash
    git checkout main
    git merge feature
    ```
    *"Fast-forward" 메시지가 뜨면 성공입니다.*
