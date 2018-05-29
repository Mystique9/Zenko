#!/bin/sh

echo "$(env)"
echo "helm upgrade ciutil
          --install orbit-simulator/orbit-simulator
          --wait $(./ci_env.sh orbit-simulator)"

helm upgrade ciutil --install orbit-simulator/orbit-simulator --wait $(./ci_env.sh orbit-simulator)"
