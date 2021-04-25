#Git brach in prompt

function parse_git_branch(){

git branch 2> /dev/null | sed -n -e 's/^\*\(.*\)/[\1]/p'}

setopt prompt_subst
export PROMPT='%n %B%F{40}%1~%f%b%F{39}$(parse_git_branch)%f $%b '

}


