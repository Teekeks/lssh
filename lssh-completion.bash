#!/usr/bin/env bash

_complete_profile()
{
      COMPREPLY=($(compgen -W "$(lssh profile list simple)" "$1"))
}

_complete_config()
{
      COMPREPLY=($(compgen -W "$(lssh config show simple)" "$1"))
}

_lssh_completions()
{
  local cur="${COMP_WORDS[$COMP_CWORD]}" prev

  if [ "$COMP_CWORD" -eq "1" ]; then
    COMPREPLY=($(compgen -W "connect profile config" "${COMP_WORDS[1]}"))
  elif [ "$COMP_CWORD" -eq "2" ]; then
    # we are on the second argument
    prev="${COMP_WORDS[1]}"
    if [[ $prev == "connect" ]] || [[ $prev == "c" ]]; then
      _complete_profile "${COMP_WORDS[2]}"
    elif [[ $prev == "profile" ]]; then
      COMPREPLY=($(compgen -W "show create list" "${COMP_WORDS[2]}"))
    elif [[ $prev == "config" ]]; then
      COMPREPLY=($(compgen -W "set get show open" "${COMP_WORDS[2]}"))
    fi
  elif [ "$COMP_CWORD" -eq "3" ]; then
    # we are on the third argument
    prev="${COMP_WORDS[2]}"
    snd="${COMP_WORDS[1]}"
    if [[ $snd == "profile" ]] && ( [[ $prev == "show" ]] || [[ $prev == "edit" ]] || [[ $prev == "open" ]]); then
      _complete_profile "${COMP_WORDS[3]}"
    elif [[ $snd == "config" ]] && [[ $prev == "set" ]]; then
      _complete_config "${COMP_WORDS[3]}"
    elif [[ $snd == "config" ]] && [[ $prev == "get" ]]; then
      _complete_config "${COMP_WORDS[3]}"
    fi

  fi
}

complete -F _lssh_completions lssh
